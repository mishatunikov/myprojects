import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handler, admin_handler
from keyboards.set_menu import set_main_menu
from middlewares.check_sub import CheckSubscription
import logging
from db import db
from fsm.fsm import storage

logger = logging.getLogger()


async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    dp = Dispatcher(storage=storage)
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token, parse_mode='html')
    await set_main_menu(bot)
    dp.message.middleware(CheckSubscription())
    dp.include_router(admin_handler.router)
    dp.include_router(user_handler.router)
    await db.db_start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
