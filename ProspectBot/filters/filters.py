from aiogram.types import Message
from states.states import db_clients

def can_calculate(message: Message):
    return db_clients[message.from_user.id]['calculate'] and \
        all(map(lambda m: m.isdigit(), message.text.split()))