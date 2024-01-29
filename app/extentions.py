
import motor.motor_asyncio
from config.db_config import DATABASE_URL
client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
database = client.interviews