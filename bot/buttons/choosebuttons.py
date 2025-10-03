# Подключение клавиатуры внизу(кнопки)
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton
# Подключение кнопок
from bot.buttons.usersbuttons import Buttons
# Библиотека для логирования
import logging
# Импорт класса работающего с базой данных
from database.selectdates import selectdatesfromDB

def returnreplymarkup(role, id_user):
    # Объявление класса с кнопками
    buttons = Buttons()
    # Создание меню
    kb_list = [[]]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )

    # Класс для работы с Базой Данных
    dbclass = selectdatesfromDB()

    match(role):
        # Возвратные данные для городов
        case "registrationtowns":
            datesfromdb = dbclass.selecttowns()
            if len(datesfromdb) % 2 == 0:
                for index in range(0, len(datesfromdb), 2):
                    kb_list.append([KeyboardButton(text = datesfromdb[index].name), KeyboardButton(text = datesfromdb[index+1].name)])
            else:
                for element in datesfromdb:
                    kb_list.append([KeyboardButton(text = element.name)])

        # Возвратные данные для типов спорта
        case "registrationtypesport":
            datesfromdb = dbclass.selectypessport()
            if len(datesfromdb) % 2 == 0:
                for index in range(0, len(datesfromdb), 2):
                    kb_list.append([KeyboardButton(text = datesfromdb[index].name), KeyboardButton(text = datesfromdb[index+1].name)])
            else:
                for element in datesfromdb:
                    kb_list.append([KeyboardButton(text = element.name)])

        # Возвратные данные для уровня спорта
        case "registrationleveltraining":
            datesfromdb = dbclass.selectleveltraining()
            for element in datesfromdb:
                    kb_list.append([KeyboardButton(text = element.name)])

        # Возвратные данные для вида спорта
        case "registrationplacetraining":
            datesfromdb = dbclass.selectplacetraining()
            for element in datesfromdb:
                kb_list.append([KeyboardButton(text = element.name)])

        # Возвратные данные для вида аккаунта
        case "registrationtypeaccaunt":
            datesfromdb = dbclass.selecttypeaccaunt()
            for element in datesfromdb:
                kb_list.append([KeyboardButton(text = element.name)])

        # Возвратные данные по выбору картинки
        case "registrationimageaccaunt":
            pass
            #kb_list.append([KeyboardButton(text = "Стандартная фотография")])

        # Возвратные данные по описанию
        case "registrationdiscription":
            kb_list.append([KeyboardButton(text = "Сгенерируем описание за тебя")])

        # Возвращаем данные после ввода описания
        case "registrationfinal":
            kb_list.append([buttons.savedatestodatabase])
            kb_list.append([buttons.dataediting])

        # Новый пользователь
        case _:
            kb_list.append([buttons.registrationnewuser])
            kb_list.append([buttons.buttonurlgroup])

    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )

def returninlinemarkup(role, id_user):
    # Объявление класса с кнопками
    buttons = Buttons()
    # Создание кнопок
    kb_list = [[]]
    match (role):

        case _:
            kb_list.append([buttons.buttoninluneurlgroup])

    return InlineKeyboardMarkup(
        inline_keyboard = kb_list)