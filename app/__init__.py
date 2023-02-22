import os
from app.operators.example_operator import ExampleOperator
from app.contexts.example_context import ExampleContext

from app.configs.config_parser import BASE_PATH, config_module


EXAMPLE_PATH = os.path.join(BASE_PATH, "app", "roles", "example")

config = config_module.Config()

example_operator = ExampleOperator(EXAMPLE_PATH, ExampleContext)
