# Библиотека для асинхронного кода
import asyncio
# Из файла create_bot подгружаем bot
from create_bot import bot, dp
# Установка стартовых команд бота
from bot.startmenu import set_default_commands
# Обработка стартовых команд бота
from bot.startcommands import start_router
# Импорт базового класса Base
from database.baseclass import Base
# Импорт функции создания всех таблиц в БД
from database.tablesclasses import create_all_databases
# Импорт роутера который отвечает за взаимодействие с пользователем
from bot.users.commandsusers import commandsrouter

async def main():
    # Подключаем роутер, который отвечает за обработку первоначальных сообщений
    dp.include_router(start_router)
    # Подключаем роутер, который отвечает за работу с сообщений от клиентов клиентами
    dp.include_router(commandsrouter)
    # Удаляем webhook (рекомендация)
    await bot.delete_webhook(drop_pending_updates=True)
    # Подгружаем первоначальные команды
    await set_default_commands(bot)
    # Вызываем базовый класс для работы с БД и выполняем метод
    dbclass = Base()
    if dbclass.checkdatabase() == True:
        pass
    else:
        create_all_databases()
    # Начинаем постоянный опрос бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())