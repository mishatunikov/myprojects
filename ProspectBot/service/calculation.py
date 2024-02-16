'''Пакет с модулями для реализации какой-то бизнес-логики бота.'''
from math import ceil
from aiogram.types import Message

from db import db


# ¥
async def calculate_cost(cost_yuan: str, message: Message) -> str:
    if all(map(str.isdigit, cost_yuan.split())):
        exchange_rate = await db.give_rate()
        current_commission = await db.give_commission()
        cost = [ceil(ceil(max(exchange_rate * int(c) * (current_commission / 100 + 1), exchange_rate *
                              int(c) + 400)) / 100) * 100 if int(c) else 0 for c in cost_yuan.split()]
        if len(cost) > 1:
            s = lambda p: f'{p[0]}. Стоимость товара без учета доставки: <b>{p[1]} ₽</b>'
            return '\n\n'.join(map(s, enumerate(cost, 1))) + f'\n\nСуммарная стоимость: <b>{sum(cost)} ₽</b>'
        else:
            s = lambda p: f'Стоимость товара без учета доставки: <b>{p} ₽</b>'
            return '\n\n'.join(map(s, cost))
    else:
        await message.answer(text='Неккоректный ввод.\n'
                                    'Повторите попытку.')



    # return s(ceil(ceil(cost[0]) / 100) * 100)
