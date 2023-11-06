from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.lexicon import KEYBOARD
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def create_keyboard_start(text: str) -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*[KeyboardButton(text=i) for i in KEYBOARD[text]], width=2)
    return kb_builder.as_markup(resize_keyboard=True,
                                one_time_keyboard=True)


