# Импорт библиотеки для работы с ботом
from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons
# Библиотека для логирования
import logging

# Импорт класса отвечающего за работу с таблицей Users
from database.tablesclasses import checkuserformdatabase, selectdatesfromdatabasebyrole
# Импорт функций для возврата кнопок
from bot.buttons.choosebuttons import returnreplymarkup
searchrouter = Router()
buttons = Buttons()

# Функция отправки сообщения о подходящих анкетах в базе
@searchrouter.message(F.text == buttons.textfindtrainer)
async def sendtelegramchannel(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindtrainer}.")
    # Проверка нахождения пользователя в базе
    if checkuserformdatabase(message.from_user.id) == True:
        # Получаем данные из базы данных
        datesfromdb = selectdatesfromdatabasebyrole('trainer')
        for element in datesfromdb:
            name = element.first_name + " " + element.middle_name + " " + element.last_name
            raiting = element.rating
            if element.id_telegram == 0:
                urlforcontact = "tg://user?id=" + str(element.id_telegram)
                urlphoto = "database/images/startimage.png"
            else:
                urlforcontact = "tg://user?id=" + str(element.id_telegram)
                urlphoto = "database/images/users/" + str(element.id_telegram) + ".png"
            print(name, "\t", raiting, "\t\t", urlforcontact, "\t", urlphoto)
    else:
        await message.answer("Не могу найти ваш аккаунт в базе.\nДавайте заведём его!",
                             reply_markup=returnreplymarkup("newuser", message.from_user.id))