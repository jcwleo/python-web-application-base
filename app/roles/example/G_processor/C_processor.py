from app.roles import Actor
from app.agents.example_agent import ExampleAgent
from app.agents import call_parallel_agent


class Processor(Actor):
    def act(self, context):
        example_agent = ExampleAgent()
        result_dict = example_agent.execute(context)

        # 병렬 호출은 원할시에는 call_parallel_agent() 사용

        context.response.update({"agentResult": result_dict})
        context.response.update({"query": context.request.query})
