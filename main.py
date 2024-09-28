import asyncio
import logging
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from telegram.handlers.get_article import main_router

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(name)s - "
                           "(%(filename)s).%(funcName)s(%(lineno)d) - "
                           "%(message)s")


bot = Bot(token='7913452277:AAH1sOZp3yoPlejsqDKMaWo2yUUfENXtmdw',
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
dp["bot_started"] = datetime.now().strftime("%Y-%m-%d %H:%M")

dp.include_routers(main_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)

    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types())

    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
