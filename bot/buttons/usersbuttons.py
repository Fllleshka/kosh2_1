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
    # Найти тренера
    textfindtrainer = "Найти тренера"
    checkfindtrainer = KeyboardButton(text=textfindtrainer)
    # Найти партнёра
    textfindstalls = "Найти партнёра для занятий спортом"
    checkfindstalls = KeyboardButton(text=textfindstalls)
    # Участие в соревнованиях
    textparticipation = "Принять участие в соревнованиях"
    checkparticipation = KeyboardButton(text=textparticipation)

    # Стрелочка влево (предыдущий вариант)
    textpreviousbutton = "<--"
    previousbutton = InlineKeyboardButton(text = textpreviousbutton,
                                          callback_data = 'previos')
    # Стрелочка вправо (следующий вариант)
    textnextbutton = "-->"
    nextbutton = InlineKeyboardButton(text = textnextbutton,
                                          callback_data = 'next')