import uvicorn
import os
from fastapi import Depends, FastAPI

from app.routers.example import api_router
from app.routers.info import info_router
from app.routers.webdemo import webdemo_router

app = FastAPI()


app.include_router(api_router)
app.include_router(info_router)
app.include_router(webdemo_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
