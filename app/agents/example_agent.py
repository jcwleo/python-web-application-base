from app.agents import Agent
from requests import Request
from dataclasses import asdict
from urllib.parse import urlencode
import json
from app import config


class ExampleAgent(Agent):
    RETRY_MAX = 3
    url = config.example_api_host
    timeout = 3
    method = "GET"
