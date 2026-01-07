from tortoise import Tortoise
import config

async def init_db():
    await Tortoise.init(config=config.DB_CONFIG)
    await Tortoise.generate_schemas()
    print("Database initialized")
    await Tortoise.close_connections()

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_db())