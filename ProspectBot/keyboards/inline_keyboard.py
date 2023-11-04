from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, URLS


async def inline_keyboard_cost() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text=LEXICON['back'], callback_data='back'),
                     InlineKeyboardButton(text=LEXICON['calculate_again'], callback_data='calculate_again'),
                     InlineKeyboardButton(text=LEXICON['order'], url='https://t.me/prospecthelp')])
    kb_builder.adjust(2)
    return kb_builder.as_markup()

async def inline_keyboard_using_app() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text=LEXICON['using_app'], url=URLS['using_app']),
                     InlineKeyboardButton(text=LEXICON['ios'], url=URLS['ios']),
                     InlineKeyboardButton(text=LEXICON['android'], url=URLS['android']),
                     InlineKeyboardButton(text=LEXICON['back'], callback_data='back')])
    kb_builder.adjust(1, 2, 1)
    return kb_builder.as_markup()

async def inline_keyboard_order() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text=LEXICON['how_order'], url=URLS['order']),
                     InlineKeyboardButton(text=LEXICON['back'], callback_data='back')])
    kb_builder.adjust(1, 2, 1)
    return kb_builder.as_markup()

async def inline_keyboard_faq() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(*[InlineKeyboardButton(text=LEXICON['faq'], url=URLS['faq']),
                     InlineKeyboardButton(text=LEXICON['back'], callback_data='back')])
    kb_builder.adjust(1, 2, 1)
    return kb_builder.as_markup()

async def inline_keyboard_about() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    kb_builder.add(InlineKeyboardButton(text=LEXICON['back'], callback_data='back'))
    return kb_builder.as_markup()