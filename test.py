from dotenv import load_dotenv, find_dotenv
import os
from pathlib import Path

# カレントディレクトリ & .env の場所確認
print("cwd:", os.getcwd())
print("find_dotenv():", find_dotenv())

# test.py と同じ階層の .env を明示的に指定
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / ".env"
print("env_path:", env_path)

load_dotenv(env_path)  # ここで .env を読み込む

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

print("API_KEY:", repr(api_key))
print("API_SECRET:", repr(api_secret))
