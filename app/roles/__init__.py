from app.contexts import BaseContext


class Actor:
    def __init__(self) -> None:
        self.skip_actor_in_sub_role = False

    def before_act(self, context: BaseContext):
        pass

    def act(self, context: BaseContext):
        pass

    def after_act(self, context: BaseContext):
        pass

    @staticmethod
    def match_function(context):
        return True
