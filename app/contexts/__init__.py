from typing import Any, List
from pydantic import BaseModel
from datetime import datetime

from dataclasses import dataclass, asdict, field


class BaseContext:
    def __init__(self) -> None:
        # self.request = dict()
        self.response = dict()
        self.request = None

    def bake_context(self, request: BaseModel) -> None:
        self.request = request
        self.request_dict = request.dict()
