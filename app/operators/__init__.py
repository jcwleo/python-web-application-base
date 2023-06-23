import os
from app.contexts import BaseContext
from pydantic import BaseModel
from app.roles import Actor
import importlib
from app.configs.config_parser import BASE_PATH


class BaseOperator:
    def __init__(self, role_name: str, context_cls: BaseContext) -> None:
        self.actors = self.load_actor(role_name)
        self.context_cls = context_cls

    def before_operator(self, request: BaseModel) -> None:
        self.context = self.context_cls()
        self.context.bake_context(request=request)

    def operator(self) -> None:
        # TODO: role 파일 실행할 수 있는 단계
        # TEST
        before_actor_instance = None
        for actor in self.actors:
            sub_role_name = actor.__module__.split(".")[-2]
            if before_actor_instance:
                if before_actor_instance.skip_actor_in_sub_role:
                    before_sub_role_name = before_actor_instance.__module__.split(".")[-2]
                    if before_sub_role_name == sub_role_name:
                        continue

            if not actor.match_function(self.context):
                # TODO: match function 매칭 여부 로깅
                continue
            actor_instance = actor()
            actor_instance.before_act(self.context)
            actor_instance.act(self.context)
            actor_instance.after_act(self.context)
            before_actor_instance = actor_instance

    def after_operator(self) -> None:
        pass

    @staticmethod
    def load_actor(role_name: str) -> list[object]:
        """
        각 operator별 작성되어있는 role을 import 한다.

        Args:
            role_name (str): 현재 operator/role name
        Returns:
            actor_class_list (list[object]): 등록 가능한 actor들의 list
        """
        class_list = []

        for root, directories, files in os.walk(role_name):
            for filename in sorted(files):
                filepath = os.path.join(root, filename)
                actor_path = os.path.abspath(filepath)
                if "__init__.py" in actor_path or "__pycache__" in actor_path:
                    continue

                rel_actor_path = os.path.relpath(actor_path, BASE_PATH)
                module_name = rel_actor_path.replace("/", ".").replace(".py", "")
                module = importlib.import_module(module_name)

                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and (obj != Actor) and issubclass(obj, Actor):
                        class_list.append(obj)

        class_list = sorted(class_list, key=lambda x: x.__module__)
        for c in class_list:
            print(c)
        return class_list
