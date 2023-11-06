from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from lexicon.lexicon import LEXICON
from keyboards.inline_keyboard import subscribe
from handlers.user_handler import back

class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[[Message], Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
            ) -> Any:
        chat_member = await event.bot.get_chat_member(chat_id='@prospect_community',
                                                      user_id=event.from_user.id)
        if chat_member.status == 'left':
            await event.answer(text=LEXICON['not_sub'],
                               reply_markup=await subscribe())

        else:
            return await handler(event, data)
