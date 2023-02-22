from pydantic import BaseModel


class ExampleRequest(BaseModel):
    query: str
    meta: dict
