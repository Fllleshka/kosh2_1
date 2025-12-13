# Импорт библиотеки для работы с ботом
import json
from cgi import print_environ_usage
from gc import callbacks

from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons
# Библиотека для логирования
import logging

# Импорт класса отвечающего за работу с таблицей Users
from database.tablesclasses import checkuserformdatabase, selectdatesfromdatabasebyrole
# Импорт функций для возврата кнопок
from bot.buttons.choosebuttons import returnreplymarkup, returninlinemarkup

from create_bot import bot

searchrouter = Router()
buttons = Buttons()

# Функция отправки сообщения о подходящих анкетах в базе
@searchrouter.message(F.text == buttons.textfindtrainer)
@searchrouter.message(F.text == buttons.textfindstalls)
async def find(message: Message):
    # Логирование нажатия на кнопку
    if message.text == buttons.textfindtrainer:
        logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindtrainer}.")
        # Получаем данные из базы данных
        table = 'trainer'
    else:
        logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindstalls}.")
        # Получаем данные из базы данных
        table = 'athlete'
    # Проверка нахождения пользователя в базе
    if checkuserformdatabase(message.from_user.id) == True:

        # Формируем данные для отправки
        datesfromdb = selectdatesfromdatabasebyrole(table, message.from_user.id)
        datatosend = selectdates(datesfromdb, 0)

        # Распределяем полученные данные для отправки
        photofile = types.FSInputFile(path = datatosend["urlphoto"])
        texttocaption = "🏆  " + str(datatosend["raiting"]) + "\n\n" + datatosend["name"]
        markup = returninlinemarkup('carusel',
                                    datatosend["urlforcontact"],
                                    datesfromdb, datatosend["previndex"],
                                    datatosend["nextindex"],
                                    datatosend["currentindex"],
                                    table)

        # Отправка сообщения
        await message.answer_photo(photo = photofile,
                                   caption = texttocaption,
                                   reply_markup=markup)

    else:
        await message.answer("Не могу найти ваш аккаунт в базе.\nДавайте заведём его!",
                             reply_markup=returnreplymarkup("newuser", message.from_user.id))

# Функция обработки нажатия кнопки next, previos
@searchrouter.callback_query(F.data.startswith('previos'))
@searchrouter.callback_query(F.data.startswith('next'))
async def nextform(callback: types.CallbackQuery):
    # Разбираем данные
    callbackdata = callback.data.split(":")
    # Название таблицы
    table = callbackdata[2]
    # Получаем данные из базы данных
    datesfromdb = selectdatesfromdatabasebyrole(callbackdata[2], callback.message.from_user.id)
    # Формируем данные для отправки
    datatosend = selectdates(datesfromdb, int(callbackdata[1]))
    # Распределяем полученные данные для отправки
    photofile = types.FSInputFile(path=datatosend["urlphoto"])
    texttocaption = "🏆  " + str(datatosend["raiting"]) + "\n\n" + datatosend[
        "name"]
    # Получаем кнопки внизу анкеты
    markup = returninlinemarkup('carusel', datatosend["urlforcontact"],
                                datesfromdb, datatosend["previndex"],
                                datatosend["nextindex"],
                                datatosend["currentindex"],
                                table)

    # Удаление сообщения
    await bot.delete_message(
            chat_id = callback.message.chat.id,
            message_id = callback.message.message_id)
    # Отправка нового
    await bot.send_photo(
            chat_id = callback.message.chat.id,
            photo = photofile,
            caption = texttocaption,
            reply_markup = markup)

# Функция выборки данных
def selectdates(data, index):
    returndict = dict()
    elem = data[index]

    # Получаем имя
    name = elem.first_name + " " + elem.middle_name + " " + elem.last_name
    returndict["name"] = name

    # Добавляем рейтинг
    raiting = elem.rating
    returndict["raiting"] = raiting

    # Добавляем предыдущую анкету
    if index == 0:
        returndict["previndex"] = len(data)-1
    else:
        returndict["previndex"] = index - 1

    # Добавляем следующую анкету
    if index == len(data)-1:
        returndict["nextindex"] = 0
    else:
        returndict["nextindex"] = index + 1

    # Добавляем текущую анкету
    returndict["currentindex"] = index

    # Добавляем ссылку на профиль
    returndict["urlforcontact"] = "tg://user?id=" + str(elem.id_telegram)

    # Добавляем ссылку на фото
    starturlphoto = "database/images/"
    if elem.id_telegram == 0:
        returndict["urlphoto"] = starturlphoto + "startimage.png"
    else:
        returndict["urlphoto"] = starturlphoto + "users/" + str(elem.id_telegram) + ".png"

    # Возврат всех данных
    return returndict