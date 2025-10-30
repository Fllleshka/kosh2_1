# Импорт библиотеки для работы с ботом
from gc import callbacks

from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
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
async def sendtelegramchannel(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textfindtrainer}.")
    # Проверка нахождения пользователя в базе
    if checkuserformdatabase(message.from_user.id) == True:
        # Получаем данные из базы данных
        datesfromdb = (selectdatesfromdatabasebyrole('trainer'))
        allcontacts = len(datesfromdb)
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
        markup = returninlinemarkup('carusel', urlforcontact, allcontacts, index)
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
                             reply_markup=returnreplymarkup("newuser", message.from_user.id))

# Функция обработки нажатия кнопки previos
@searchrouter.callback_query(F.data.startswith('previos'))
async def previosform(message: Message):
    print("Previus!!!")
    print("ID Callback previos", message.message.message_id)

# Функция обработки нажатия кнопки next
@searchrouter.callback_query(F.data.startswith('next'))
async def previosform(message: Message):
    print("NEXT!!!")
    print("ID Callback next", message.message.message_id)