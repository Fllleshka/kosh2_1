# Подключение клавиатуры внизу(кнопки)
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton
# Подключение кнопок
from bot.buttons.usersbuttons import Buttons
# Библиотека для логирования
import logging
# Импорт класса работающего с базой данных
from database.selectdates import selectdatesfromDB
# Подключение кнопок
from aiogram.types import InlineKeyboardButton

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

        # Возвратные данные для новых пользователей
        case "newuser":
            kb_list.append([buttons.registrationnewuser])
            kb_list.append([buttons.buttonurlgroup])

        # Возвратные денные для зарегистрированных пользователей
        case "registereduser":
            kb_list.append([buttons.checkprofiletoother])
            kb_list.append([buttons.editprofile])
            kb_list.append([buttons.checkfindtrainer])
            kb_list.append([buttons.checkfindstalls])
            kb_list.append([buttons.checkparticipation])

        # Возвратные данные после редактирования данных профиля
        case "editdatesinprofile":
            kb_list.append([buttons.checkprofiletoother])

        case "urlcompetitiontable":
            kb_list.append([buttons.checkparticipation])

        case _:
            kb_list.append([buttons.checkaccaunt])

    return ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Воспользуйтесь меню:"
    )

def returninlinemarkup(role, urltouser, datafromdb = None, previosindex = 0, nextindex = 0, currtentindex = 0):
    # Объявление класса с кнопками
    buttons = Buttons()
    # Создание кнопок
    kb_list = [[]]
    match (role):
        case "carusel":

            # Стрелочка влево (предыдущий вариант)
            textpreviousbutton = "<--"
            callbackdataprevios = 'previos:' + str(previosindex)
            previousbutton = InlineKeyboardButton(text=textpreviousbutton,
                                                  callback_data=callbackdataprevios)

            # Стрелочка вправо (следующий вариант)
            textnextbutton = "-->"
            callbackdatanext = 'next:' + str(nextindex)
            nextbutton = InlineKeyboardButton(text=textnextbutton,
                                              callback_data=callbackdatanext)

            # Добавление центральной секции
            textcenter = str(currtentindex) + "/" + str(len(datafromdb))
            centersection = InlineKeyboardButton(text=textcenter,
                                                 callback_data='center')

            # Добавление нижней секции
            contactbutton = InlineKeyboardButton(text='Связь', url=urltouser)

            # Добавление первой строки
            kb_list.append([previousbutton, centersection, nextbutton])
            # Добавление второй строки
            kb_list.append([contactbutton])

        case "changedatesinprofile":
            # Кнопка редактирования имени
            kb_list.append([buttons.editname])
            # Кнопка редактирования фамилии
            kb_list.append([buttons.editlastname])
            # Кнопка редактирования отчества
            kb_list.append([buttons.editmiddlename])
            # Кнопка редактирования даты рождения
            kb_list.append([buttons.editbirthdate])
            # Кнопка редактирования города
            kb_list.append([buttons.edittown])
            # Кнопка редактирования типа спорта
            kb_list.append([buttons.edittypesport])
            # Кнопка редактирования уровня подготовки
            kb_list.append([buttons.editlevelsport])
            # Кнопка редактирования места проведения
            kb_list.append([buttons.editplacetrain])
            # Кнопка редактирования картинки профиля
            kb_list.append([buttons.editimageprofile])
            # Кнопка редактирования описания
            kb_list.append([buttons.editdescription])
        case _:
            kb_list.append([buttons.buttoninluneurlgroup])

    return InlineKeyboardMarkup(
        inline_keyboard = kb_list)