from pydantic import BaseSettings
import os

current_dir = os.path.dirname(os.path.abspath(__file__)).split(os.path.sep)[-1]


class Config(BaseSettings):
    env: str = current_dir
    app_name: str = "padk_example"
    admin_email: str = "jcwleo@naver.com"
    version: str = "v1.0"
    example_api_host = "https://dummyjson.com/products/1"
