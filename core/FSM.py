from aiogram.fsm.storage.mongo import MongoStorage
from aiogram.fsm.state import default_state, State, StatesGroup
from core.db import MONGO_DB_URL

storage = MongoStorage.from_url(MONGO_DB_URL)

class User(StatesGroup):
    # Состояние по умолчанию (начальное состояние)
    default = default_state

    # Примеры состояний
    waiting_for_name = State()  # Ожидание ввода имени
    waiting_for_age = State()  # Ожидание ввода возраста
    waiting_for_email = State()  # Ожидание ввода email
    waiting_for_confirmation = State()  # Ожидание подтверждения
    

class ADMINpanel(StatesGroup):
    MENU = State()
    REQUEST = State()
    ACCEPT_LIST = State()
    REJECT_LIST = State()
    WAIT_USER_ID = State()
    WAIT_ADD_USER = State()