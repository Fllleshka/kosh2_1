# Импорт библиотеки для работы с ботом
from aiogram import Router, F
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons
# Импорт библиотеки для работы с ботом
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
# Библиотека для логирования
import logging
# Импорт бота (для скачивания картинки)
from create_bot import bot as BBot
# Библиотека для работы с Ботом
import os.path

# Импорт сообщений для пользователей
from database.dates import bot_messages
# Импорт функций для возврата кнопок
from bot.buttons.choosebuttons import returnreplymarkup, returninlinemarkup
# Импорт функции добавления данных в базу данных
from database.tablesclasses import insert_user_dates_in_database

registration = Router()
buttons = Buttons()

# Класс состояний
class Registration(StatesGroup):
    telegramid = State()
    firstname = State()
    middlename = State()
    lastname = State()
    age = State()
    town = State()
    typesport = State()
    levelsport = State()
    place = State()
    typeaccaunt = State()
    imageuser = State()
    discription = State()
    insertdates = State()

# Функция Подбора правильного сообщения в зависимости от статуса
def choosetext(argument, dates=None):
    match(argument):
        case Registration.firstname:
            text = bot_messages.messagefirstname
        case Registration.lastname:
            text = bot_messages.messagelastname
        case Registration.middlename:
            text = bot_messages.messagemiddlename
        case Registration.age:
            text = bot_messages.messagebirthdate
        case Registration.town:
            text = bot_messages.messagechoosetown
        case Registration.typesport:
            text = bot_messages.messagechoosetypesport
        case Registration.levelsport:
            text = bot_messages.messagechooselevel
        case Registration.place:
            text = bot_messages.messagechooseplace
        case Registration.typeaccaunt:
            text = bot_messages.messagechooseaccaunttype
        case Registration.imageuser:
            text = bot_messages.messageimageuser
        case Registration.discription:
            text = bot_messages.messagedescription
        case _:
            text = bot_messages.messagefinalregistration
            text += "\n\n"
            text += "[" + str(dates['telegramid']) + "]\n"
            text += "Имя:\n        " + dates['firstname'] + "\n"
            text += "Фамилия:\n        " + dates['lastname'] + "\n"
            text += "Отчество:\n        " + dates['middlename'] + "\n"
            text += "Дата рождения:\n        " + dates['age'] + "\n"
            text += "Город:\n        " + dates['town'] + "\n"
            text += "Тип спорта:\n        " + dates['typesport'] + "\n"
            text += "Уровень подготовки:\n        " + dates['levelsport'] + "\n"
            text += "Место подготовки:\n        " + dates['place'] + "\n"
            text += "Тип аккаунта:\n        " + dates['typeaccaunt'] + "\n"
            text += "Картинка:\n        " + dates['imageuser'] + "\n"
            text += "Описание:\n        " + dates['discription'] + "\n"
    return text

# Функция регистрации в базе данных, ввод Имени
@registration.message(F.text == buttons.textregistrationnewuser)
async def registration_firstname(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.registrationnewuser}.")
    statefunction = Registration.firstname
    # Сохраняем telegramid
    await state.update_data(telegramid = message.from_user.id)
    # Установка состояния ввода Имени
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    await message.answer(text, reply_markup = ReplyKeyboardRemove())

# Функция ввода Фамилии
@registration.message(Registration.firstname, F.text)
async def registration_lastname(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил имя пользователя: {message.text}")
    statefunction = Registration.lastname
    # Сохраняем введённое имя
    await state.update_data(firstname = message.text)
    # Установка состояния ввода Фамилии
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    await message.answer(text)

# Функция ввода Отчества
@registration.message(Registration.lastname, F.text)
async def registration_middlename(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил фамилию пользователя: {message.text}")
    statefunction = Registration.middlename
    # Сохраняем введённую фамилию
    await state.update_data(lastname = message.text)
    # Установка состояния ввода Отчества
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    await message.answer(text)

# Функция ввода возраста
@registration.message(Registration.middlename, F.text)
async def registration_age(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил отчество пользователя: {message.text}")
    statefunction = Registration.age
    # Сохраняем введённое отчество
    await state.update_data(middlename = message.text)
    # Установка состояния ввода даты рождения
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    await message.answer(text)

# Функция ввода возраста
@registration.message(Registration.age, F.text)
async def registration_age(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил дату рождения: {message.text}")
    statefunction = Registration.town
    # Сохраняем введённое дату рождения
    await state.update_data(age = message.text)
    # Установка состояния ввода Города
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationtowns", None)
    await message.answer(text, reply_markup = markup)

# Функция ввода вида спорта
@registration.message(Registration.town, F.text)
async def registration_typesport(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил город: {message.text}")
    statefunction = Registration.typesport
    # Сохраняем введённый город
    await state.update_data(town = message.text)
    # Установка состояния ввода типа спорта
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationtypesport", None)
    await message.answer(text, reply_markup=markup)

# Функция ввода уровня подготовки
@registration.message(Registration.typesport, F.text)
async def registration_leveltraining(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил тип спорта: {message.text}")
    statefunction = Registration.levelsport
    # Сохраняем введённый тип спорта
    await state.update_data(typesport = message.text)
    # Установка состояния ввода типа спорта
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationleveltraining", None)
    await message.answer(text, reply_markup=markup)

# Функция ввода места тренировок
@registration.message(Registration.levelsport, F.text)
async def registration_placetraining(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил уровень подготовки: {message.text}")
    statefunction = Registration.place
    # Сохраняем введённый уровень подготовки
    await state.update_data(levelsport = message.text)
    # Установка состояния ввода места тренировок
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationplacetraining", None)
    await message.answer(text, reply_markup=markup)

# Функция ввода типа аккаунта
@registration.message(Registration.place, F.text)
async def registration_typeaccaunt(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил места тренировок: {message.text}")
    statefunction = Registration.typeaccaunt
    # Сохраняем введённое место тренировок
    await state.update_data(place = message.text)
    # Установка состояния выбора типа аккаунта
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationtypeaccaunt", None)
    await message.answer(text, reply_markup=markup)

# Функция ввода картинки аккаунта
@registration.message(Registration.typeaccaunt, F.text)
async def registration_immageaccaunt(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил тип аккаунта: {message.text}")
    statefunction = Registration.imageuser
    # Сохраняем введённый тип аккаунта
    await state.update_data(typeaccaunt = message.text)
    # Установка состояния выбора картинки аккаунта
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationimageaccaunt", None)
    await message.answer(text, reply_markup = ReplyKeyboardRemove())

# Функция ввода описания к анкете
@registration.message(Registration.imageuser, F.photo)
async def registration_discription(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил картинку: {message.text}")
    statefunction = Registration.discription
    # Сохраняем введённую картинку
    data = await state.get_data()
    telegramid = str(data['telegramid'])
    url = "database/images/users/" + telegramid + ".png"
    fileinfo = message.photo[-1]
    await BBot.download(fileinfo, destination=url)
    textuser = "Фотография загружена" if os.path.exists(url) == True else "Ошибка загрузки фотографии"
    await state.update_data(imageuser = textuser)
    # Установка состояния выбора картинки аккаунта
    await state.set_state(statefunction)
    # Отправка сообщения
    text = choosetext(statefunction)
    markup = returnreplymarkup("registrationdiscription", None)
    await message.answer(text, reply_markup=markup)

# Функция сохранения описания к анкете
@registration.message(Registration.discription, F.text)
async def registration_final(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} отправил описание к своей анкете: {message.text}")
    statefunction = Registration.insertdates
    # Сохраняем введённое описание
    await state.update_data(discription=message.text)
    # Установка состояния сохранения данных об аккаунте
    await state.set_state(statefunction)
    # Отправка сообщения
    dates = await state.get_data()
    text = choosetext(None, dates)
    markup = returnreplymarkup("registrationfinal", None)
    await message.answer(text, reply_markup=markup)

# Функция отправки данных в базу данных
@registration.message(Registration.insertdates, F.text)
async def insert_dates_in_database(message: Message, state: FSMContext):
    logging.info(f"Пользователь {message.from_user.id} нажал на кнопку: {message.text}")
    # Сохраняем данные в базу данных
    dates = await state.get_data()
    insert_user_dates_in_database(dates)
    # Обнуляем состояние
    await state.clear()
    # Отправляем сообщение об успешной регистрации
    await message.answer("Аккаунт успешно зарегистрирован",
                         reply_markup=returninlinemarkup(None,
                                                         message.from_user.id))
