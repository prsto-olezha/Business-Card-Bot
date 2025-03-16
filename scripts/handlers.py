from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import core.keyboard as keyboards
import core.FSM as FSM
from core.models import User_model
import core.db as db
from core.logger import logger
#========================================

router = Router()

@router.message(CommandStart())
async def start(msg: Message, state: FSMContext):
    await msg.answer(f"Привет, {msg.from_user.first_name}!", reply_markup=keyboards.inline_get_main_menu_keyboard())
    await state.set_state(FSM.User.default)
    
    if not await db.find_user_by_id(msg.from_user.id):   
        user_obj = User_model(
            id=msg.from_user.id,
            user_name=msg.from_user.username,
            first_name=msg.from_user.first_name,
            last_name=msg.from_user.last_name
            )
        await User_model.insert_one(user_obj)
        logger.info(f"Новый пользователь: {user_obj.model_dump_json()}", )
    
@router.callback_query(F.data == "profile")
async def get_profile(callback: CallbackQuery, state: FSMContext):
    user_obj = await db.find_user_by_id(callback.from_user.id)  
    await callback.message.answer(f"{user_obj}", reply_markup=keyboards.inline_get_main_menu_keyboard())