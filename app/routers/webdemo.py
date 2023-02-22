from functools import lru_cache

from fastapi import Depends, Request
from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
import os
from app import config
from app.configs.config_parser import BASE_PATH

webdemo_router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(BASE_PATH, "app", "frontend"))


@webdemo_router.get("/webdemo")
async def webdemo(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
