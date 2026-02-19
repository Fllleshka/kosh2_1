# Библиотека для работы с Ботом
from aiogram import Router, F,types
from aiogram.types import Message
# Импорт кнопок для админской панели
from bot.buttons.adminbuttons import AdminButtons as adminbuttons
from bot.buttons.usersbuttons import Buttons
from bot.buttons.choosebuttons import returnreplymarkup
from database.baseclass import baseclass

from datetime import datetime
# Библиотеки для работы с файлами
import os
import shutil

# Создаём роутер
adminsfunctionsrouter = Router()

@adminsfunctionsrouter.message(F.text == Buttons.textautorisationadmin)
async def savedatabase(message: Message):
    text = "Вы вошли как администратор.\nФункционал отображается для администратора."
    markup = returnreplymarkup("adminsbutton", message.from_user.id)
    await message.answer(text, reply_markup=markup)

@adminsfunctionsrouter.message(F.text == adminbuttons.textsavedatabase)
async def savedatabase(message: Message):
    # Формируем название файла backup
    date = datetime.now()
    newnamefile = f"database_backup_{str(date.day)}.{date.month}.{date.year}_{date.hour}.{date.minute}.db"
    # Проверка файла базы данных на нахождение

    pathtodatabase = baseclass.databaseurl()
    print(pathtodatabase)
    print(os.path.exists(pathtodatabase))
    pathtobackup = "database/backups/" + newnamefile
    print(pathtobackup)
    try:
        shutil.copyfile(pathtodatabase, pathtobackup)
        text = f"База данных сохранена.\nНазвание файла:\n{newnamefile}"
        await message.answer(text)
    except Exception as e:
        print(e)
