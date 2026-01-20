# Подключение кнопок
from aiogram.types import KeyboardButton, InlineKeyboardButton

class AdminButtons:
    textsavedatabase = "Сохранить копию БД"
    savedatabase = KeyboardButton(text=textsavedatabase)