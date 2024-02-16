from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, URLS


async def inline_keyboard_cost() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text=LEXICON['back'], callback_data='back'),
                     InlineKeyboardButton(text=LEXICON['calculate_again'], callback_data='calculate_again')])
    kb_builder.adjust(2, 1)
    return kb_builder.as_markup()


async def inline_keyboard_cancel() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(InlineKeyboardButton(text='Отмена', callback_data='back'))
    return kb_builder.as_markup()


async def inline_keyboard_parameters() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text='Изменить курс', callback_data='change_rate'),
                     InlineKeyboardButton(text='Изменить комиссию', callback_data='change_commission'),
                     InlineKeyboardButton(text=LEXICON['back'], callback_data='back')])
    kb_builder.adjust(1)
    return kb_builder.as_markup()


async def inline_keyboard_newsletter() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text='Сделать рассылку', callback_data='make_newsletter'),
                     InlineKeyboardButton(text=LEXICON['back'], callback_data='back')])
    return kb_builder.as_markup()


async def inline_keyboard_confirmnslt() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text='✅', callback_data='confirm_newsletter'),
                     InlineKeyboardButton(text='❌', callback_data='cancel_newsletter')])
    return kb_builder.as_markup()
