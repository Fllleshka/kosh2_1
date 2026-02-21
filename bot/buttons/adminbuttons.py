# Подключение кнопок
from aiogram.types import KeyboardButton, InlineKeyboardButton

class AdminButtons:
    textsavedatabase = "Сохранить копию БД"
    savedatabase = KeyboardButton(text=textsavedatabase)
    textalltrainer = "Все тренера"
    alltrainer = KeyboardButton(text=textalltrainer)
    textallathletes = "Все спортсмены"
    allathletes = KeyboardButton(text=textallathletes)
