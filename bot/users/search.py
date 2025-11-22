# Импорт библиотеки для работы с ботом
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

# Машина состояний для анкет
class formStates(StatesGroup):
    def __init__(self):
        self.dates = selectdatesfromdatabasebyrole('trainer')
        startstate = State()
        nextstate = State()
        previosstate = State()

    def insertdates(self):
        for elem in self.dates:
            name = elem.first_name + " " + elem.middle_name + " " + elem.last_name
            raiting = elem.rating
            if elem.id_telegram == 0:
                urlforcontact = "tg://user?id=" + str(elem.id_telegram)
                urlphoto = "database/images/startimage.png"
            else:
                urlforcontact = "tg://user?id=" + str(elem.id_telegram)
                urlphoto = "database/images/users/" + str(
                    elem.id_telegram) + ".png"
            print("====================")
            print(name)
            print("\t", raiting)
            print("\t", urlforcontact)
            print("\t", urlphoto)
            print("====================")

# Функция отправки сообщения о подходящих анкетах в базе
@searchrouter.message(F.text == buttons.textfindtrainer)
@searchrouter.message(F.text == buttons.textfindstalls)
async def find(message: Message):
    # Логирование нажатия на кнопку
    if message.text == buttons.textfindtrainer:
        logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindtrainer}.")
        # Получаем данные из базы данных
        datesfromdb = selectdatesfromdatabasebyrole('trainer')
    else:
        logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindstalls}.")
        # Получаем данные из базы данных
        datesfromdb = selectdatesfromdatabasebyrole('athlete')
    # Проверка нахождения пользователя в базе
    if checkuserformdatabase(message.from_user.id) == True:
        # Инициируем машину состояний
        states = formStates()
        states.insertdates()

        firstelem = datesfromdb[0]
        index = datesfromdb.index(firstelem)
        name = firstelem.first_name + " " + firstelem.middle_name + " " + firstelem.last_name
        raiting = firstelem.rating
        if firstelem.id_telegram == 0:
            urlforcontact = "tg://user?id=" + str(firstelem.id_telegram)
            urlphoto = "database/images/startimage.png"
        else:
            urlforcontact = "tg://user?id=" + str(firstelem.id_telegram)
            urlphoto = "database/images/users/" + str(
                firstelem.id_telegram) + ".png"
        markup = returninlinemarkup('carusel', urlforcontact, datesfromdb)
        textmessage = "🏆  " + str(raiting) + "\n\n" + name
        photofile = types.FSInputFile(path=urlphoto)

        '''for element in datesfromdb:
            name = element.first_name + " " + element.middle_name + " " + element.last_name
            raiting = element.rating
            if element.id_telegram == 0:
                urlforcontact = "tg://user?id=" + str(element.id_telegram)
                urlphoto = "database/images/startimage.png"
            else:
                urlforcontact = "tg://user?id=" + str(element.id_telegram)
                urlphoto = "database/images/users/" + str(element.id_telegram) + ".png"
            markup = returninlinemarkup('carusel', urlforcontact, allcontacts, 0)
            textmessage = "🏆  " + str(raiting) + "\n\n" + name
            photofile = types.FSInputFile(path=urlphoto)
            print(name, "\t", raiting, "\t\t", urlforcontact, "\t", urlphoto)
        '''

        send_message = await message.answer_photo(photo = photofile,
                                   caption = textmessage,
                                   reply_markup=markup)
        print("ID отправленного сообщения: ",send_message.message_id)

    else:
        await message.answer("Не могу найти ваш аккаунт в базе.\nДавайте заведём его!",
                             reply_markup=returnreplymarkup("newuser", message.from_user.id, ))

# Функция обработки нажатия кнопки previos
@searchrouter.callback_query(F.data.startswith('previos'))
async def previosform(message: Message, callback_query: types.CallbackQuery):
    # Получаем данные из базы данных
    datesfromdb = (selectdatesfromdatabasebyrole('trainer'))

    print("Previus!!!")
    print("ID Callback previos", message.message.message_id)
    await bot.delete_message(chat_id=message.message.chat.id, message_id=message.message.message_id)


    textmessage = "🏆  " + str(raiting) + "\n\n" + name
    #await bot.send_photo(chat_id=message.message.chat.id,)

# Функция обработки нажатия кнопки next
@searchrouter.callback_query(F.data.startswith('next'))
async def previosform(message: Message):
    print("NEXT!!!")
    print("ID Callback next", message.message.message_id)
    await message.ed