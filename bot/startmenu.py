from aiogram.types import BotCommand, BotCommandScopeDefault
import logging

async def set_default_commands(bot):
    commands = [
        BotCommand(command = "start", description = 'Начать сначала'),
        BotCommand(command = "help", description = 'Техническая помощь'),
        BotCommand(command = "helpfounder", description = 'Помощь по сообществу'),
        BotCommand(command = "admin", description = "Админка")
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
    logging.info("Команды успешно добавлены")