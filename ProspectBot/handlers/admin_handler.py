from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON
from aiogram import Router, F
from keyboards.keyboard import create_keyboard_start_adm
from keyboards.inline_keyboard_adm import inline_keyboard_parameters, inline_keyboard_cost, inline_keyboard_cancel, \
    inline_keyboard_newsletter, inline_keyboard_confirmnslt
from service.calculation import calculate_cost
from service.send_newsletter import send_newsletter
from aiogram.fsm.context import FSMContext
from fsm import fsm
from aiogram.filters import StateFilter
from db import db
from filters import filters


router = Router()
# router.message.filter(filters.filter_adm(F.from_user.id))

# Использование фильтров в router
router.message.filter(filters.message_admin_filter)
router.callback_query.filter(filters.callback_query_admin_filter)


# Сделать проверку на статусы при нажатии на оставшейся клавиатуре
# Обработка команды /start
@router.message(CommandStart())
async def process_start_command(message: Message, state: FSMContext):
    await state.clear()
    await db.add_client(message.chat.id, message.from_user.username)
    await message.delete()
    await message.answer(text=LEXICON[message.text](message),
                         reply_markup=create_keyboard_start_adm(message.text))


# Обработка команды /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text=LEXICON['/help'], reply_markup=ReplyKeyboardRemove())


# Обработки кнопки рассчитать стоимость
@router.message(F.text == 'Рассчитать стоимость')
async def start_calculate(message: Message | CallbackQuery, state: FSMContext):
    await state.set_state(fsm.FSMadmins.calculation)
    if isinstance(message, Message):
        s = f'{LEXICON["parameters"](await db.give_rate(), await db.give_commission())}'
        await message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                  '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>',
                             reply_markup=await inline_keyboard_cancel())
    else:
        await message.message.answer(text='<b>Введите стоимость в юанях.</b>\n\n'
                                          '<i>*Используйте <b>пробел</b> для рассчета нескольких позиций.</i>',
                                     reply_markup=await inline_keyboard_cancel())


# Обработка данных цены
@router.message(StateFilter(fsm.FSMadmins.calculation))
async def give_cost(message: Message, state: FSMContext):
    cost = await calculate_cost(message.text, message)
    keyboard = await inline_keyboard_cost()
    await message.answer(text=f'Курс: <b>1¥ | {await db.give_rate()}₽</b>\n' \
                              f'Комиссия: <b>{await db.give_commission()}%</b>\n\n')
    await message.answer(text=f'{cost}', reply_markup=keyboard)
    await state.set_state()


# Отправляет на повторный рассчет цены
@router.callback_query(F.data == 'calculate_again')
async def calculate_again(callback: CallbackQuery, state: FSMContext):
    # await callback.message.delete()
    await callback.message.delete_reply_markup()
    await start_calculate(callback, state)


@router.callback_query(F.data == 'back')
async def back(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    # await callback.message.delete()
    await callback.message.delete_reply_markup()
    await callback.message.answer(text=LEXICON['main_menu'],
                                  reply_markup=create_keyboard_start_adm('/start'))


@router.message(F.text == 'Курс | Комиссия')
async def rate(message: Message):
    await message.answer(text=LEXICON['parameters'](await db.give_rate(), await db.give_commission()),
                         reply_markup=await inline_keyboard_parameters())


@router.callback_query(F.data == 'change_rate')
async def change_rate(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    await state.set_state(fsm.FSMadmins.change_rate)
    await callback.message.answer(text='Введите новый курс 💱')


@router.message(StateFilter(fsm.FSMadmins.change_rate))
async def process_change_rate(message: Message, state: FSMContext):
    if filters.check_nums(message.text):
        await db.change_rate(float(message.text))
        await message.answer(text=LEXICON['parameters'](await db.give_rate(), await db.give_commission()),
                             reply_markup=await inline_keyboard_parameters())
        await state.clear()
    else:
        await message.answer(text='Некорректный ввод. \n\nДробь через ".", если что.')


@router.callback_query(F.data == 'change_commission')
async def change_rate(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    await state.set_state(fsm.FSMadmins.change_commission)
    await callback.message.answer(text='Введите новую комиссию %')


@router.message(StateFilter(fsm.FSMadmins.change_commission))
async def process_change_rate(message: Message, state: FSMContext):
    if filters.check_nums(message.text):
        await db.change_commission(float(message.text))
        await message.answer(text=LEXICON['parameters'](await db.give_rate(), await db.give_commission()),
                             reply_markup=await inline_keyboard_parameters())
        await state.clear()
    else:
        await message.answer(text='Некорректный ввод. \n\nДробь через ".", если что.')



@router.message(F.text == 'Статьи')
async def rate(message: Message):
    await message.answer(text=
                         f"<b>1.</b> <b><a href='https://telegra.ph/Ispolzovanie-prilozheniya-Poizon-06-25'>" \
                         f"Использование приложения.</a></b>✈️\n" \
                         f"<i><a href='tg://user?id={'https://apps.apple.com/app/id1012871328'}'>Скачать IOS</a></i> | "
                         f"<i><a href='tg://user?id={'https://www.anxinapk.com/rj/12201303.html'}'>Скачать ANDROID</a></i>\n\n" \
                         f"<b>2.</b> <b><a href='https://telegra.ph/Kak-sdelat-zakaz-06-25'>" \
                         f"Как сделать заказ?</a></b>✈️\n\n" \
                         f"<b>3.</b> <b><a href='https://telegra.ph/FAQ-06-25-11'>"
                         f"Часто задаваемые вопросы</a></b>✈️",
                         reply_markup=create_keyboard_start_adm('/start'))


@router.message(F.text == 'Рассылка')
async def rate(message: Message):
    await message.answer(text=f'Количество активных пользователей: <b>{await db.give_active_users()}</b>',
                         reply_markup=await inline_keyboard_newsletter())


@router.callback_query(F.data == 'make_newsletter')
async def make_newsletter(callback: CallbackQuery, state: FSMContext):
    await state.set_state(fsm.FSMadmins.newsletter)
    await callback.message.answer(text='Введите текст рассылки.')


@router.message(StateFilter(fsm.FSMadmins.newsletter))
async def confirmation_newsletter(message: Message):
    await message.send_copy(chat_id=message.chat.id, reply_markup=await inline_keyboard_confirmnslt())


@router.callback_query(F.data == 'confirm_newsletter')
async def make_newsletter(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete_reply_markup()
    await state.clear()
    await send_newsletter(callback.bot, callback.message.message_id)
    await callback.message.answer(text=f'<b>Пользователи успешно оповещены.</b>\n\n'
                                       f'Количество активных пользователей: <b>{await db.give_active_users()}</b>',
                                  reply_markup=await inline_keyboard_newsletter())
    await state.clear()


@router.callback_query(F.data == 'cancel_newsletter')
async def make_newsletter(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(text=f'Количество активных пользователей: <b>{await db.give_active_users()}</b>',
                                  reply_markup=await inline_keyboard_newsletter())
