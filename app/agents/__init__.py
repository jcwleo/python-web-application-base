from requests import Request, Session, Response
from requests.exceptions import RequestException
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logger = logging.getLogger(__name__)


class Agent:
    RETRY_MAX = 3
    session = Session()
    url: str = ""
    timeout: float = 0.5
    method: str = "POST"

    def __init__(self):
        self.result = None

    def make_request(self, context) -> Request:
        params = self.make_params(context)
        headers = self.make_headers(context)
        data_json_str = json.dumps(params, ensure_ascii=False).encode("utf-8")
        return Request(method=self.method, url=self.url, headers=headers, data=data_json_str)

    @staticmethod
    def make_params(context):
        return {}

    @staticmethod
    def make_headers(context):
        return {"Content-Type": "application/json"}

    def execute(self, context) -> Response:
        request_obj = self.make_request(context)
        response_dict = {"result": None, "error": ""}
        retry_cnt = 0
        error = None

        while retry_cnt < self.RETRY_MAX:
            try:
                response = Agent.session.send(request_obj.prepare(), timeout=self.timeout)
                response.raise_for_status()
                response_json = response.json()
                break
            except RequestException as e:
                error = e
                logger.error("An error occurred:", error)
                retry_cnt += 1
            except Exception as e:
                error = e
                logger.error("An error occurred:", error)
                retry_cnt += 1

        if retry_cnt == self.RETRY_MAX:
            response_dict["error"] = error
            return response_dict

        response_dict["result"] = response_json
        self.result = response_json
        return response_dict

    def is_valid_result(self):
        return True

    @property
    def valid(self):
        return self.is_valid_result()


def call_parallel_agent(agent_list, context):
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(agent.execute, context) for agent in agent_list]
        results = [future.result() for future in as_completed(futures)]
    return results


if __name__ == "__main__":
    agent_1 = Agent("https://reqres.in/api/users")
    agent_2 = Agent("https://example.com/")

    print(call_parallel_agent([agent_1, agent_2], {}))
