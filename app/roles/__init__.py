from app.contexts import BaseContext


class Actor:
    def before_act(self, context: BaseContext):
        pass

    def act(self, context: BaseContext):
        pass

    def after_act(self, context: BaseContext):
        pass

    @staticmethod
    def match_function(context):
        return True
