from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.context import FSMContext

redis = Redis(host='localhost')
storage = RedisStorage(redis=redis)


class FSMclient(StatesGroup):
    main_menu = State()
    calculation = State()


class FSMadmins(StatesGroup):
    calculation = State()
    change_rate = State()
    change_commission = State()
    newsletter = State()


