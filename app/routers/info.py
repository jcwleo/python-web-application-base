from functools import lru_cache

from fastapi import Depends
from fastapi import APIRouter

from app import config

info_router = APIRouter()


@info_router.post("/info")
async def info():
    return {
        "app_name": config.app_name,
        "env": config.env,
        "admin_email": config.admin_email,
        "version": config.version,
    }
