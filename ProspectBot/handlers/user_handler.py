from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from aiogram import Router, F
from keyboards.keyboard import create_keyboard_start_usr
from keyboards.inline_keyboard_usr import inline_keyboard_cost, inline_keyboard_using_app, inline_keyboard_about, \
    inline_keyboard_order, inline_keyboard_faq, inline_keyboard_cancel
from service.calculation import calculate_cost
from aiogram.fsm.context import FSMContext
from fsm import fsm
from aiogram.filters import StateFilter
from db import db


router = Router()


# Сделать проверку на статусы при нажатии на оставшейся клавиатуре
# Обработка команды /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await db.add_client(message.chat.id, message.from_user.username)
    await state.clear()
    await message.delete()
    await message.answer(text=LEXICON[message.text](message),
                         reply_markup=create_keyboard_start_usr(message.text))


# Обработка команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=LEXICON['/help'], reply_markup=ReplyKeyboardRemove())


# Обработки кнопки рассчитать стоимость
@router.message(F.text == 'Рассчитать стоимость')
async def start_calculate(message: Message | CallbackQuery, state: FSMContext):
    await state.set_state(fsm.FSMclient.calculation)
    if isinstance(message, Message):
        await message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                  '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>')
    else:
        await message.message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                          '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>')


# Обработка данных цены
@router.message(StateFilter(fsm.FSMclient.calculation))
async def give_cost(message: Message, state: FSMContext):
    cost = await calculate_cost(message.text, message)
    keyboard = await inline_keyboard_cost()
    await message.answer(text=cost, reply_markup=keyboard)
    await state.set_state()


# Отправляет на повторный рассчет цены
@router.callback_query(F.data == 'calculate_again')
async def calculate_again(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    await start_calculate(callback, state)


@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete_reply_markup()
    await callback.message.answer(text=LEXICON['main_menu'],
                                  reply_markup=create_keyboard_start_usr('/start'))


@router.message(F.text == 'Как пользоваться Poizon?')
async def using_app(message: Message):
    kb = await inline_keyboard_using_app()
    await message.answer(text=LEXICON[message.text], reply_markup=kb)


@router.message(F.text == 'Как сделать заказ?')
async def using_app(message: Message):
    kb = await inline_keyboard_order()
    await message.answer(text=LEXICON[message.text], reply_markup=kb)


@router.message(F.text == 'О нас')
async def using_app(message: Message):
    kb = await inline_keyboard_about()
    await message.answer(text=LEXICON[message.text], reply_markup=kb)


@router.message(F.text == 'FAQ')
async def using_app(message: Message):
    kb = await inline_keyboard_faq()
    await message.answer(text=LEXICON[message.text], reply_markup=kb)


@router.callback_query(F.data == 'delivery_cost')
async def delivery_cost(callback: CallbackQuery):
    await callback.answer(text=LEXICON['Какова цена доставки?'], show_alert=True)
