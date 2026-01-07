from tortoise import Tortoise
import config

async def init_db():
    await Tortoise.init(config=config.DB_CONFIG)
    await Tortoise.generate_schemas()
    print("Database initialized")