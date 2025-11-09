# Импорт библиотеки для работы с ботом
from aiogram import Router, F, types
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
# Библиотека для логирования
import logging
# Импорт кнопок
from bot.buttons.usersbuttons import Buttons
# Импорт класса с сообщениями
from database.dates import bot_messages
# Импорт функций для возврата кнопок
from bot.buttons.choosebuttons import returnreplymarkup, returninlinemarkup
# Импорт бота для отправки сообщений
from create_bot import bot as BBot
# Импорт функции вставки данных в таблицу
from database.tablesclasses import updatedatesfromusers
# Роутер
editprofile = Router()
buttons = Buttons()

# Состояния для редактирования
class EditStates(StatesGroup):
    name = State()
    middlename = State()
    lastname = State()
    birthdate = State()

# Обработка кнопки "Изменить профиль"
@editprofile.message(F.text == buttons.texteditprofile)
async def funeditprofile(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал на кнопку {buttons.texteditprofile}.")
    textmessage = bot_messages.messageeditprofile1
    await message.answer(textmessage, reply_markup = ReplyKeyboardRemove())
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await message.answer(textmessage,reply_markup=markup)

# Функция редактирования имени
@editprofile.callback_query(F.data == "editname")
async def editname_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditname}.")
    statefunction = EditStates.name
    await state.set_state(statefunction)
    await call.message.answer("Введите новое Имя")
@editprofile.message(EditStates.name, F.text)
async def editname_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новое имя: {message.text}")
    # Вставляем данные в базу данных
    newname = message.text
    updatedatesfromusers(message.from_user.id, 'first_name', newname)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    await BBot.send_message(message.chat.id, text="Ваше имя изменено.", reply_markup = ReplyKeyboardRemove())
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования фамилии
@editprofile.callback_query(F.data == "editlastname")
async def editlastname_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditlastname}.")
    statefunction = EditStates.lastname
    await state.set_state(statefunction)
    await call.message.answer("Введите новую Фамилию")
@editprofile.message(EditStates.lastname, F.text)
async def editlastname_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новую фамилию: {message.text}")
    # Вставляем данные в базу данных
    newlastname = message.text
    updatedatesfromusers(message.from_user.id, 'last_name', newlastname)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    await BBot.send_message(message.chat.id, text="Ваша фамилия изменена.", reply_markup = ReplyKeyboardRemove())
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования отчества
@editprofile.callback_query(F.data == "editmiddlename")
async def editmiddlename_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditlastname}.")
    statefunction = EditStates.middlename
    await state.set_state(statefunction)
    await call.message.answer("Введите новое Отчество")
@editprofile.message(EditStates.middlename, F.text)
async def editmiddlename_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новое отчество: {message.text}")
    # Вставляем данные в базу данных
    newmiddlename = message.text
    updatedatesfromusers(message.from_user.id, 'middle_name', newmiddlename)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    await BBot.send_message(message.chat.id, text="Ваше отчество изменено.", reply_markup = ReplyKeyboardRemove())
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования даты рождения
@editprofile.callback_query(F.data == "editbirthdate")
async def editbirthdate_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditbirthdate}.")
    statefunction = EditStates.birthdate
    await state.set_state(statefunction)
    await call.message.answer("Введите новую дату рождения")
@editprofile.message(EditStates.birthdate, F.text)
async def editbirthdate_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новую дату рождения: {message.text}")
    # Вставляем данные в базу данных
    birthdate = message.text
    updatedatesfromusers(message.from_user.id, 'birth_date', birthdate)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    await BBot.send_message(message.chat.id, text="Ваша дата рождения изменена.", reply_markup = ReplyKeyboardRemove())
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования города

# Функция редактирования типа спорта

# Функция редактирования уровня подготовки

# Функция редактирования места проведения

# Функция редактирования картинки профиля

# Функция редактирования описания