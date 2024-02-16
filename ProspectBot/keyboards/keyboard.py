from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from lexicon.lexicon import KEYBOARD_USER, KEYBOARD_ADMIN
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def create_keyboard_start_usr(text: str) -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*[KeyboardButton(text=i) for i in KEYBOARD_USER[text]], width=2)
    return kb_builder.as_markup(resize_keyboard=True,
                                one_time_keyboard=True)


def create_keyboard_start_adm(text: str) -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    kb_builder.row(*[KeyboardButton(text=i) for i in KEYBOARD_ADMIN[text]], width=2)
    return kb_builder.as_markup(resize_keyboard=True,
                                one_time_keyboard=True)