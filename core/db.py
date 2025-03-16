from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from core.config import MONGO_DB_CONNECT
from core.models import User_model

# mongo
MONGO_DB_URL = f"mongodb://{MONGO_DB_CONNECT['username']}:{MONGO_DB_CONNECT['password']}@{MONGO_DB_CONNECT['host']}:{MONGO_DB_CONNECT['port']}/"

async def init_mongo_db(models):
    client = AsyncIOMotorClient(MONGO_DB_URL, uuidRepresentation="standard")
    await init_beanie(client[MONGO_DB_CONNECT['db_Users']], document_models=models)
    
    
#======================================

async def find_user_by_id(user_id: int):
    user = await User_model.find_one(User_model.id == user_id)
    return user