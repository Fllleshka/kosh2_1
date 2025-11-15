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
from database.tablesclasses import updatedatesfromusers, find_id_in_table
# Библиотека для работы с файлами
import os.path

# Роутер
editprofile = Router()
buttons = Buttons()

# Состояния для редактирования
class EditStates(StatesGroup):
    name = State()
    middlename = State()
    lastname = State()
    birthdate = State()
    town = State()
    typesport = State()
    levelsport = State()
    plase = State()
    image = State()
    description = State()

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
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваше имя изменено.", reply_markup = markup)
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
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваша фамилия изменена.", reply_markup = markup)
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
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваше отчество изменено.", reply_markup = markup)
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
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваша дата рождения изменена.", reply_markup = markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования города
@editprofile.callback_query(F.data == "edittown")
async def edittown_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.textedittown}.")
    statefunction = EditStates.town
    await state.set_state(statefunction)
    markup = returnreplymarkup('registrationtowns', call.message.from_user.id)
    await call.message.answer("Выберите новый город из списка ниже", reply_markup = markup)
@editprofile.message(EditStates.town, F.text)
async def edittown_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новый город: {message.text}")
    # Получаем нужное id города
    town = message.text
    id_town = find_id_in_table('towns', town)
    # Вставляем данные в базу данных
    updatedatesfromusers(message.from_user.id, 'town_date', id_town)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваш город изменен.", reply_markup = markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования типа спорта
@editprofile.callback_query(F.data == "edittypesport")
async def edittypesport_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.textedittypesport}.")
    statefunction = EditStates.typesport
    await state.set_state(statefunction)
    markup = returnreplymarkup('registrationtypesport', call.message.from_user.id)
    await call.message.answer("Выберите новый тип спорта из списка ниже", reply_markup = markup)
@editprofile.message(EditStates.typesport, F.text)
async def edittypesport_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новый тип спорта: {message.text}")
    # Получаем нужное id типа спорта
    typesport = message.text
    id_type = find_id_in_table('kinds', typesport)
    # Вставляем данные в базу данных
    updatedatesfromusers(message.from_user.id, 'type_sport', id_type)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваш тип спорта изменен.", reply_markup = markup)

    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования уровня подготовки
@editprofile.callback_query(F.data == "editlevelsport")
async def editlevelsport_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditlevelsport}.")
    statefunction = EditStates.levelsport
    await state.set_state(statefunction)
    markup = returnreplymarkup('registrationleveltraining', call.message.from_user.id)
    await call.message.answer("Выберите новый уровень подготовки из списка ниже", reply_markup = markup)
@editprofile.message(EditStates.levelsport, F.text)
async def editlevelsport_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новый уровень подготовки: {message.text}")
    # Получаем нужное id типа спорта
    levelsport = message.text
    id_type = find_id_in_table('levels', levelsport)
    # Вставляем данные в базу данных
    updatedatesfromusers(message.from_user.id, 'level_sport', id_type)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваш уровень подготовки изменен.", reply_markup = markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования места проведения
@editprofile.callback_query(F.data == "editplacetrain")
async def editplacetrain_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditplacetrain}.")
    statefunction = EditStates.plase
    await state.set_state(statefunction)
    markup = returnreplymarkup('registrationplacetraining', call.message.from_user.id)
    await call.message.answer("Выберите новое место проведения из списка ниже", reply_markup = markup)
@editprofile.message(EditStates.plase, F.text)
async def editplacetrain_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новое место проведения: {message.text}")
    # Получаем нужное id места проведения
    placetrain = message.text
    id_place = find_id_in_table('places', placetrain)
    # Вставляем данные в базу данных
    updatedatesfromusers(message.from_user.id, 'place_train', id_place)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваше место проведения изменено.", reply_markup = markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)

# Функция редактирования картинки профиля
@editprofile.callback_query(F.data == "editimageprofile")
async def editimageprofile_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditimageprofile}.")
    statefunction = EditStates.image
    await state.set_state(statefunction)
    await call.message.answer("Загрузите новую картинку", reply_markup = ReplyKeyboardRemove())
@editprofile.message(EditStates.image, F.photo)
async def editimageprofile_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} загрузил новую картинку: {message.text}")
    # Сохраняем введённую картинку
    telegramid = str(message.from_user.id)
    url = "database/images/users/" + telegramid + ".png"
    fileinfo = message.photo[-1]
    await BBot.download(fileinfo, destination=url)
    textuser = "Фотография загружена" if os.path.exists(url) == True else "Ошибка загрузки фотографии"
    await state.update_data(imageuser=textuser)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id,
                            text="Ваша фотография изменена",
                            reply_markup=markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile', message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,
                            reply_markup=markup)

# Функция редактирования описания
@editprofile.callback_query(F.data == "editdescription")
async def editdescription_callback(call: CallbackQuery, state: FSMContext):
    logging.info(f"Пользователь {call.message.from_user.id} нажал на кнопку {buttons.texteditdescription}.")
    statefunction = EditStates.description
    await state.set_state(statefunction)
    await call.message.answer("Введите новое описание:")
@editprofile.message(EditStates.description, F.text)
async def editdescription_insertdatesindb(message: Message, state: FSMContext):
    # Логирование
    logging.info(f"Пользователь {message.from_user.id} ввёл новое описание: {message.text}")
    # Вставляем данные в базу данных
    newdescription = message.text
    updatedatesfromusers(message.from_user.id, 'description', newdescription)
    # Обнуляем состояние
    await state.clear()
    # Отправка сообщения 1
    markup = returnreplymarkup("editdatesinprofile", message.chat.id)
    await BBot.send_message(message.chat.id, text="Ваше описание изменено.", reply_markup = markup)
    # Отправка сообщения 2
    textmessage = bot_messages.messageeditprofile2
    markup = returninlinemarkup('changedatesinprofile',message.from_user.id)
    await BBot.send_message(message.chat.id, text=textmessage,reply_markup=markup)