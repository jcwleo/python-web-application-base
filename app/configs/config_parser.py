import os
import importlib

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 기본 환경값 가져오기
env = os.environ.get("DEPLOY_ENV", "dev")

config_path = os.path.join("app", "configs", env, "config.py")
config_module = importlib.import_module(config_path.replace(os.path.sep, ".").replace(".py", ""))
