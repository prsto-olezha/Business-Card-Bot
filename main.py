import asyncio
from core.logger import logger
from create_bot import bot, dp
from core.db import init_mongo_db

#===============================

from scripts.handlers import router
from scripts.admin_handlers import router as admin_router

#==============================

from core.models import Applicant_model, User_model

#==============================
mongo_models = [
    Applicant_model,
    User_model,
    ]


async def main():
    dp.include_router(router)
    dp.include_router(admin_router)
    await init_mongo_db(models=mongo_models)
    await bot.delete_webhook(drop_pending_updates=True)
    logger.info("Bot activated!")
    await dp.start_polling(bot)

    
    
async def on_startup():
    await asyncio.gather(
        asyncio.create_task(main()),
        )
    
    
if __name__ == "__main__":
    try:
        asyncio.run(on_startup())
    except KeyboardInterrupt:
        logger.info("Bot deactivated!")
    except Exception as e:
        logger.error(f"Error: {e}")
        