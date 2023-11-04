'''Пакет с модулями для реализации какой-то бизнес-логики бота.'''
from math import ceil
exchange_rate = 14.6


async def calculate_cost(cost_yuan: int) -> str:
    cost = max(exchange_rate * cost_yuan * 1.09, exchange_rate * cost_yuan + 400)
    return f'Стоимость товара без учета доставки: <b>' \
           f'{ceil(ceil(cost)/100) * 100} ₽</b>'
