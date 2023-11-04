'''Модуль для установки команд в нативную кнопку "Menu" вашего бота.'''

from aiogram import Bot
from aiogram.types import BotCommand

from lexicon.lexicon import MENU_COMMAND


# Функция для настройки кнопки Menu бота
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command=command, description=description)
        for command, description in MENU_COMMAND.items()
    ]
    await bot.set_my_commands(main_menu_commands)