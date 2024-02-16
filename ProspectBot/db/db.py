import sqlite3 as sq
from aiogram.types import Message
from datetime import datetime
from aiogram.fsm.context import FSMContext
from lexicon.lexicon import LEXICON

# Подключение базы, если нет файла, то создается.
db = sq.connect('tg.db')
# Курсор, выполняет основные функции
cur = db.cursor()


async def db_start():
    cur.execute("CREATE TABLE IF NOT EXISTS parameters ("
                "exchange_rate REAL,"
                "commission REAL)")

    cur.execute("CREATE TABLE IF NOT EXISTS clients ("
                "chat_id INTEGER PRIMARY KEY,"
                "username TEXT,"
                "status TEXT)")

    cur.execute("INSERT INTO parameters (exchange_rate, commission) SELECT 13, 9 "
                "WHERE NOT EXISTS (SELECT 1 FROM parameters LIMIT 1)")
    db.commit()


async def give_rate():
    rate = cur.execute('SELECT exchange_rate FROM parameters').fetchone()
    return rate[0]


async def change_rate(new_rate: int | float):
    cur.execute('UPDATE parameters SET exchange_rate=?', (new_rate,))
    db.commit()


async def give_commission():
    rate = cur.execute('SELECT commission FROM parameters').fetchone()
    return rate[0]


async def change_commission(new_commission: int | float):
    cur.execute('UPDATE parameters SET commission=?', (new_commission,))
    db.commit()

# Добить добавление в базу
async def add_client(chat_id, username):
    user = cur.execute("SELECT * FROM clients WHERE chat_id = ?", (chat_id,)).fetchone()
    if not user:
        cur.execute('INSERT INTO clients (chat_id, username) VALUES (?, ?)', (chat_id, username,))
    db.commit()


async def give_active_users():
    rate = cur.execute("SELECT COUNT(*) FROM clients WHERE chat_id NOT IN (872711036)").fetchone()
    return rate[0]


async def give_chat_id():
    chats = cur.execute("SELECT chat_id FROM clients WHERE chat_id NOT IN (872711036)").fetchall()
    return chats
