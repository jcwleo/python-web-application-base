import os
from fastapi import APIRouter
from functools import lru_cache
from app import config
from app.models.example_model import ExampleRequest

from app import example_operator

api_router = APIRouter()


@api_router.post(f"/api")
async def api(request: ExampleRequest):
    example_operator.before_operator(request)
    example_operator.operator()
    example_operator.after_operator()
    result = example_operator.context.response
    return result
