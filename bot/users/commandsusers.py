# Импорт библиотеки для работы с ботом
from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove
# Импорт движка для работы с базой
from database.baseclass import engine
from database.dates import bot_messages
# Импорт класса отвечающего за работу с таблицей Users
from database.tablesclasses import find_all_data_from_database, find_name_in_table, checkuserformdatabase
# Библиотека для логирования
import logging
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons
# Библиотека для загрузки переменных окружения из .env
from decouple import config

# Импорт функций для возврата кнопок
from bot.buttons.choosebuttons import returnreplymarkup, returninlinemarkup

commandsrouter = Router()
buttons = Buttons()

# Функция отправки сообщения о телеграмм канале
@commandsrouter.message(F.text == buttons.textrulgroup)
async def sendtelegramchannel(message: Message):
    logging.info(
        f"Пользователь {message.from_user.id} нажал на кнопку {buttons.textrulgroup}.")
    await message.answer("⬇️Вот ссылка на наш телеграмм канал⬇️", reply_markup=returninlinemarkup(None, message.from_user.id))

# Функция обработки кнопки "Мой аккаунт"
@commandsrouter.message(F.text == buttons.textcheckaccaunt)
async def checkaccaunt(message: Message):
    # Проверка нахождения пользователя в базе
    if checkuserformdatabase(message.from_user.id) == True:
        await message.answer(
            "Твой аккаунт есть в базе.\nВыбери что будем делать дальше!",
            reply_markup=returnreplymarkup("registereduser", message.from_user.id))
    else:
        await message.answer(
            "Не могу найти ваш аккаунт в базе.\nДавайте заведём его!",
            reply_markup=returnreplymarkup("newuser", message.from_user.id))

# Функция обработки кнопки "Мой профиль для других"
@commandsrouter.message(F.text == buttons.textprofiletoother)
async def myprofileforothers(message: Message):
    datesfromdb = find_all_data_from_database(message.from_user.id)
    text = "[" + str(datesfromdb.id_telegram) + "]                             🏆" + str(datesfromdb.rating) + "\n"
    text += "Имя:\n        " + datesfromdb.first_name + "\n"
    text += "Фамилия:\n        " + datesfromdb.last_name + "\n"
    text += "Отчество:\n        " + datesfromdb.middle_name + "\n"
    text += "Дата рождения:\n        " + datesfromdb.birth_date + "\n"
    text += "Город:\n        " + find_name_in_table('towns', datesfromdb.id_town) + "\n"
    text += "Тип спорта:\n        " + find_name_in_table('kinds', datesfromdb.id_type) + "\n"
    text += "Уровень подготовки:\n        " + find_name_in_table('levels', datesfromdb.id_level) + "\n"
    text += "Место подготовки:\n        " + find_name_in_table('places', datesfromdb.id_place) + "\n"
    text += "Тип аккаунта:\n        " + find_name_in_table("type", datesfromdb.id_type) + "\n"
    text += "Описание:\n        " + datesfromdb.description + "\n"
    pathtoimage = "database/images/users/" + str(message.from_user.id) + ".png"
    photo = types.FSInputFile(path=pathtoimage)
    await message.answer_photo(caption = text, photo=photo)

# Функция обработки кнопки "Принять участие в соревнованиях"
@commandsrouter.message(F.text == buttons.textparticipation)
async def take_part_competiion(message: Message):

    name = create_appeal(message)
    textmessage = f"<b>Уважаемый, {name}!</b>\n\n"
    textmessage += bot_messages.messagecompetitiontable
    photofile = types.FSInputFile(path="database/images/startimage.png")
    inline_button = [
        [types.InlineKeyboardButton(text=Buttons.textparticipation,
                                    url=config('googlesheetcompetitiontable'))]
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=inline_button)
    await message.answer_photo(caption=textmessage, photo=photofile,
                               reply_markup=markup)

# Вычисления обращения к пользователю
def create_appeal(message):
    try:
        name = message.from_user.first_name + " " + message.from_user.last_name
    except:
        name = "[Не смог определить ваше имя]"
    return name