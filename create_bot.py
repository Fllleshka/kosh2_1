# Библиотека для логирования
import logging
# Библиотека для работы с Ботом
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
# Библиотека для загрузки переменных окружения из .env
from decouple import config
# Библиотека для работы с базой данных
#from database.baseclass import Base
#from sqlalchemy import create_engine
# Настраиваем логирование
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Инициируем объект бота, передавая ему parse_mode=ParseMode.HTML по умолчанию
bot = Bot(token=config('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

# Инициируем объект бота
dp = Dispatcher()

