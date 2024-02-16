from aiogram import Bot
from itertools import chain
from db import db
from aiogram.types import Message


async def send_newsletter(bot: Bot, message_id):
    chats = chain.from_iterable(await db.give_chat_id())
    for i in chats:
        try:
            await bot.copy_message(chat_id=i, from_chat_id=872711036, message_id=message_id)
        except:
            pass
