from dataclasses import dataclass
from aiogram.types import Message

# states = {'calculate': False}
db_clients = {}

def add_client_db(message: Message):
    db_clients.setdefault(message.from_user.id, {'calculate': False})

