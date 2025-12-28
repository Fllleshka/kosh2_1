# Библиотека для работы с Ботом
from types import NoneType
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ReplyKeyboardRemove
# Библиотека для загрузки переменных окружения из .env
from decouple import config

# Импорт данный для тестовых сообщений
from database.dates import bot_messages
# Импорт класса для генерации кнопочек
from bot.buttons.choosebuttons import returnreplymarkup
# Импорт функции для обработки обращения
from bot.users.commandsusers import create_appeal
# Создаём роутер
start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    name = create_appeal(message)
    textmessage = f"<b>Привет, {name}!</b>\n\n"
    textmessage += bot_messages.welcomemessage
    photofile = types.FSInputFile(path = "database/images/startimage.png")
    markup = returnreplymarkup(None, message.from_user.id)
    await message.answer_photo(photo = photofile, caption = textmessage, reply_markup=markup)

@start_router.message(Command('help'))
async def cmd_help(message: Message):
    name = create_appeal(message)
    textmessage = f"Уважаемый, <b>{name}</b>\n\n"
    textmessage += bot_messages.helpmessage
    inline_button = [
        [types.InlineKeyboardButton(text = "Технический специалист", url = config('TECHNICALSPRC'))]
    ]
    photo = types.FSInputFile(path="database/images/developer.png")
    markup = types.InlineKeyboardMarkup(inline_keyboard = inline_button)
    await message.answer_photo(caption = textmessage, photo=photo, reply_markup=markup)

@start_router.message(Command('helpfounder'))
async def cmd_help(message: Message):
    name = create_appeal(message)
    textmessage = f"Уважаемый, <b>{name}</b>\n\n"
    textmessage += bot_messages.helpfoundermessage
    inline_button = [
        [types.InlineKeyboardButton(text=config('NAMEFOUNDER1'), url=config('FOUNDER1'))],
        [types.InlineKeyboardButton(text=config('NAMEFOUNDER2'), url=config('FOUNDER2'))]
    ]
    markup = types.InlineKeyboardMarkup(inline_keyboard=inline_button)
    await message.answer(text=textmessage, reply_markup=markup)

# Функция обработки кнопки "Админка"
@start_router.message(Command('admin'))
async def cmd_admin(message: Message):
    if (message.from_user.id == int(config("FOUNDER1TELEGRAMID"))
            or message.from_user.id == int(config("FOUNDER2TELEGRAMID"))
            or message.from_user.id == int(config("TECHNICALSPRCTELEGRAMID"))):
        textmessage = "Выберите функционал"
        markup = returnreplymarkup("admin", message.from_user.id)
        await message.answer(text = textmessage, reply_markup=markup)
    else:
        textmessage = "У вас нет доступа к этому функционалу"
        markup = returnreplymarkup(None, message.from_user.id)
        await message.answer(text = textmessage, reply_markup=markup)
