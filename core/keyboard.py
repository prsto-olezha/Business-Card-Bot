from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove

#========================================
# ReplyKeyboard example
def get_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Кнопка 1")
    builder.button(text="Кнопка 2")
    builder.button(text="Кнопка 3")
    builder.adjust(2)  # Расположить кнопки в 2 колонки
    return builder.as_markup(resize_keyboard=True)


# Inlinekeboard example
def get_inline_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Кнопка 1", callback_data="button1")
    builder.button(text="Кнопка 2", callback_data="button2")
    builder.button(text="Кнопка 3", callback_data="button3")
    builder.adjust(2)  # Расположить кнопки в 2 колонки    
    return builder.as_markup()


# Клавиатура для главного меню ==========================================================
def reply_get_main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Профиль")
    builder.button(text="Настройки")
    builder.button(text="О нас")
    builder.adjust(2)  # Располагаем кнопки в 2 колонки
    
    # Возвращаем клавиатуру с настройками
    return builder.as_markup(
        resize_keyboard=True,  # Автоматическое изменение размера клавиатуры
        one_time_keyboard=False,  # Клавиатура не исчезает после нажатия
        selective=False  # Клавиатура показывается всем пользователям
    )
    

def inline_get_main_menu_keyboard():
    builder = InlineKeyboardBuilder()
    feedback_btn = InlineKeyboardButton(text="Откликнуться", callback_data="feedback")
    profile_btn = InlineKeyboardButton(text="Профиль", callback_data="profile")
    options_btn = InlineKeyboardButton(text="Настройки", callback_data="options")
    about_us_btn = InlineKeyboardButton(text="О нас", callback_data="about_us")
    
    builder.row(feedback_btn)
    builder.row(profile_btn, options_btn)
    builder.row(about_us_btn)
    return builder.as_markup()

# Клавиатура для главного меню ==========================================================