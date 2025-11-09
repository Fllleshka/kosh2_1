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
    editname = InlineKeyboardButton(text=texteditname,
                                    callback_data='editname')
    # Кнопка редактирования фамилии
    texteditlastname = "Фамилия"
    editlastname = InlineKeyboardButton(text=texteditlastname,
                                    callback_data='editlastname')
    # Кнопка редактирования отчества
    texteditmiddlename = "Отчество"
    editmiddlename = InlineKeyboardButton(text=texteditmiddlename,
                                    callback_data='editmiddlename')
    # Кнопка редактирования даты рождения
    texteditbirthdate = "Дата рождения"
    editbirthdate = InlineKeyboardButton(text=texteditbirthdate,
                                    callback_data='editbirthdate')
    # Кнопка редактирования города
    textedittown = "Город"
    edittown = InlineKeyboardButton(text=textedittown,
                                    callback_data='edittown')
    # Кнопка редактирования типа спорта
    textedittypesport = "Спорт"
    edittypesport = InlineKeyboardButton(text=textedittypesport,
                                    callback_data='edittypesport')
    # Кнопка редактирования уровня подготовки
    texteditlevelsport = "Уровень подготовки"
    editlevelsport = InlineKeyboardButton(text=texteditlevelsport,
                                    callback_data='editlevelsport')
    # Кнопка редактирования места проведения
    texteditplacetrain = "Место проведения"
    editplacetrain = InlineKeyboardButton(text=texteditplacetrain,
                                    callback_data='editplacetrain')
    # Кнопка редактирования картинки профиля
    texteditimageprofile = "Картинка профиля"
    editimageprofile = InlineKeyboardButton(text=texteditimageprofile,
                                    callback_data='editimageprofile')
    # Кнопка редактирования описания
    texteditdescription = "Описание"
    editdescription = InlineKeyboardButton(text=texteditdescription,
                                            callback_data='editdescription')

    # Найти тренера
    textfindtrainer = "Найти тренера"
    checkfindtrainer = KeyboardButton(text=textfindtrainer)
    # Найти партнёра
    textfindstalls = "Найти партнёра для занятий спортом"
    checkfindstalls = KeyboardButton(text=textfindstalls)
    # Участие в соревнованиях
    textparticipation = "Принять участие в соревнованиях"
    checkparticipation = KeyboardButton(text=textparticipation)