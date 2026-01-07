import os
from dotenv import load_dotenv
from pathlib import Path 

load_dotenv()

# ip,端口
LLMKEY = os.getenv("LLMKEY") 
LLMURL = os.getenv("LLMURL") 
LLMMODEL = os.getenv("LLMMODEL") 

DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": os.getenv("DB_HOST"),
                "port": os.getenv("DB_PORT"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
                "database": os.getenv("DB_NAME"),
            }
        }
    },
    "apps": {
        "models": {
            "models": ["aerich.models", "memory.orm.models"],  # 你的模型
            "default_connection": "default",
        }
    },
}