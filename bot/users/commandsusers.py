# Импорт библиотеки для работы с ботом
from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove
# Библиотека для работы с базой данных
from sqlalchemy.orm import sessionmaker
# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт класса отвечающего за работу с таблицей Users
from database.tablesclasses import Users, find_all_data_from_database, find_name_in_table
# Библиотека для логирования
import logging
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons

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

# Функция отправки обработки кнопки "Мой аккаунт"
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

# Функция отправки обработки кнопки "Мой профиль для других"
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

# Функция поиска пользователя в БД
def checkuserformdatabase(userid):
    # Создаём сессию
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Делаем запрос в БД
        found_item = session.query(Users).filter_by(id_telegram = userid).first()
        # Если объект найден
        if found_item != None:
            logging.info(f"Пользователь с {userid} найден в базе")
            return True
        # Если объект не найден
        else:
            logging.info(f"Пользователь с {userid} не найден в базе")
            return False
