# Импорт библиотеки для работы с ботом
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
# Библиотека для работы с базой данных
from sqlalchemy.orm import sessionmaker
# Импорт движка для работы с базой
from database.baseclass import engine
# Импорт класса отвечающего за работу с таблицей Users
from database.tablesclasses import Users
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
