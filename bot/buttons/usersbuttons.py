# Подключение кнопок
from aiogram.types import KeyboardButton, InlineKeyboardButton
# Класс для вспомогательных ссылок
from database.dates import helpdates

class Buttons:
    # Регистрация
    textregistrationnewuser = "Зарегистрироваться"
    registrationnewuser = KeyboardButton(text=textregistrationnewuser)
    # Получение информации
    textrulgroup = "Получить полезную информацию о нас"
    buttonurlgroup = KeyboardButton(text=textrulgroup)
    # Телеграмм канал
    urlgroup = "https://t.me/koshsports"
    buttoninluneurlgroup = InlineKeyboardButton(text="Сообщениство Kosh", url=urlgroup)
    # Сохранение данный в базу
    textsavedatestodatabase = "Сохранение данных в БД"
    savedatestodatabase = KeyboardButton(text=textsavedatestodatabase)
    # Редактирование данных
    textdataediting = "Редактирование данных"
    dataediting = KeyboardButton(text=textdataediting)
    # Проверка аккаунта
    textcheckaccaunt = "Мой аккаунт"
    checkaccaunt = KeyboardButton(text=textcheckaccaunt)
    # Профиль для других
    textprofiletoother = "Мой профиль для других"
    checkprofiletoother = KeyboardButton(text=textprofiletoother)
    # Изменение данных в профиле
    texteditprofile = "Изменить профиль"
    editprofile = KeyboardButton(text=texteditprofile)
    # Кнопка редактирования имени
    texteditname = "Имя"
    editname = InlineKeyboardButton(text=texteditname, callback_data='editname')
    # Кнопка редактирования фамилии
    texteditlastname = "Фамилия"
    editlastname = InlineKeyboardButton(text=texteditlastname, callback_data='editlastname')
    # Кнопка редактирования отчества
    texteditmiddlename = "Отчество"
    editmiddlename = InlineKeyboardButton(text=texteditmiddlename,callback_data='editmiddlename')
    # Кнопка редактирования даты рождения
    texteditbirthdate = "Дата рождения"
    editbirthdate = InlineKeyboardButton(text=texteditbirthdate,
                                          callback_data='birthdate')
    #kb_list.append([buttons.])
    # Кнопка редактирования города
    #kb_list.append([buttons.])
    # Кнопка редактирования типа спорта
    #kb_list.append([buttons.])
    # Кнопка редактирования уровня подготовки
    #kb_list.append([buttons.])
    # Кнопка редактирования места проведения
    #kb_list.append([buttons.])
    # Кнопка редактирования картинки профиля
    #kb_list.append([buttons.])
    # Кнопка редактирования описания
    #kb_list.append([buttons.])

    # Найти тренера
    textfindtrainer = "Найти тренера"
    checkfindtrainer = KeyboardButton(text=textfindtrainer)
    # Найти партнёра
    textfindstalls = "Найти партнёра для занятий спортом"
    checkfindstalls = KeyboardButton(text=textfindstalls)
    # Участие в соревнованиях
    textparticipation = "Принять участие в соревнованиях"
    checkparticipation = KeyboardButton(text=textparticipation)