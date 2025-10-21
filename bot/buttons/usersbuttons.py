# Подключение кнопок
from aiogram.types import KeyboardButton, InlineKeyboardButton
# Класс для вспомогательных ссылок
from database.dates import helpdates

class Buttons:
    # Инициализация класса
    #def __init__(self):
    textregistrationnewuser = "Зарегистрироваться"
    registrationnewuser = KeyboardButton(text=textregistrationnewuser)
    textrulgroup = "Получить полезную информацию о нас"
    buttonurlgroup = KeyboardButton(text=textrulgroup)
    urlgroup = "https://t.me/koshsports"
    buttoninluneurlgroup = InlineKeyboardButton(text="Сообщениство Kosh", url=urlgroup)

    textsavedatestodatabase = "Сохранение данных в БД"
    savedatestodatabase = KeyboardButton(text=textsavedatestodatabase)
    textdataediting = "Редактирование данных"
    dataediting = KeyboardButton(text=textdataediting)

    textcheckaccaunt = "Мой аккаунт"
    checkaccaunt = KeyboardButton(text=textcheckaccaunt)

    '''
    self.btn1 = telebot.types.KeyboardButton("💪Я тренер💪")
    self.btn2 = telebot.types.KeyboardButton("🏅Я спортсмен🏅")
    self.btn3 = telebot.types.KeyboardButton("🧐Я просто интересуюсь🧐")
    self.btn4 = telebot.types.KeyboardButton("Найти тренера")
    self.btn6 = telebot.types.KeyboardButton(
        "Найти партнёра для занятий спортом")
    self.btn7 = telebot.types.KeyboardButton(
        "Принять участие в соревнованиях")

    self.btn9 = telebot.types.KeyboardButton("Мой профиль 💪")
    self.btn10 = telebot.types.KeyboardButton("Найти спортсмена")
    self.btn11 = telebot.types.KeyboardButton("Моего варианта нет")
    self.btn12 = telebot.types.KeyboardButton("Мой профиль для других")
    self.btntelegramchannel = telebot.types.InlineKeyboardButton(
        "Kosh Sports", telegrampath)
    self.competitiontable = telebot.types.InlineKeyboardButton(
        "Kosh Sports Table", googlesheetcompetitiontable)
    self.sendinformation = telebot.types.KeyboardButton(
        "Отправить данные на сервер")
    self.changeprofileinfo = telebot.types.KeyboardButton(
        "Отредактировать профиль")
    self.sendmessageadmin = telebot.types.InlineKeyboardButton("Админ",
                                                               adminchannel)
    '''