from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from aiogram import Router, F
from keyboards.keyboard import create_keyboard_start
from keyboards.inline_keyboard import inline_keyboard_cost, inline_keyboard_using_app, inline_keyboard_about, \
    inline_keyboard_order, inline_keyboard_faq, inline_keyboard_cancel
from states.states import db_clients, add_client_db
from service.service import calculate_cost
from filters.filters import can_calculate

router = Router()


# Обработка команды /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    # клиент добавляется в базу данных
    add_client_db(message)
    await message.answer(text=LEXICON[message.text](message),
                         reply_markup=create_keyboard_start(message.text))


# Обработка команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    # клиент добавляется в базу данных
    add_client_db(message)
    await message.answer(text=LEXICON['/help'], reply_markup=ReplyKeyboardRemove())


# Обработки кнопки рассчитать стоимость
@router.message(F.text == 'Рассчитать стоимость')
async def start_calculate(message: Message | CallbackQuery):
    # переводим клиента в состояние рассчета
    # Нужно добавить проверку на наличии в базе
    db_clients[message.from_user.id]['calculate'] = True
    if isinstance(message, Message):
        await message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                  '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>',
                             reply_markup=await inline_keyboard_cancel())
    else:
        await message.message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                          '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>',
                                     reply_markup=await inline_keyboard_cancel())


# Обработка данных цены
@router.message(can_calculate)
async def give_cost(message: Message):
    # рассчет цены
    cost = await calculate_cost(message.text)
    keyboard = await inline_keyboard_cost()
    await message.answer(text=cost, reply_markup=keyboard)
    db_clients[message.from_user.id]['calculate'] = False


# Отправляет на повторный рассчет цены
@router.callback_query(F.data == 'calculate_again')
async def calculate_again(callback: CallbackQuery):
    # db_clients[callback.from_user.id]['calculate'] = True
    await callback.message.delete()
    await start_calculate(callback)


@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery):
    # await callback.message.edit_text('<b>Вы вернулись в главное меню</b>')
    await callback.message.delete()
    await callback.message.answer(text=LEXICON['main_menu'],
                                  reply_markup=create_keyboard_start('/start'))


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
