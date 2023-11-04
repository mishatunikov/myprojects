'''Пакет с модулями для реализации какой-то бизнес-логики бота.'''
from math import ceil
from lexicon.lexicon import LEXICON
exchange_rate = 14.6

# ¥
async def calculate_cost(cost_yuan: str) -> str:
    s = lambda p: f'Стоимость товара без учета доставки: <b>{p} ₽</b>'
    cost = lambda c: max(exchange_rate * int(c) * 1.09, exchange_rate * int(c) + 400)
    if len(cost_yuan.split()) > 1:
        return '\n\n'.join(map(lambda x: f'<b>{x[0]}) {x[1]} ¥</b>\n{s(ceil(ceil(cost(x[1]))/100) * 100)}',
                               enumerate(cost_yuan.split(), start=1)))
    return s(ceil(ceil(cost(cost_yuan))/100) * 100)
