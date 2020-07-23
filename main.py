import logging

from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

import var
import asyncio
import os
import uvloop

from extend.massage_handler import register


async def shutdown(dispatcher: Dispatcher) -> None:
    """
    :param dispatcher:
    :return:
    """
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


def set_up_app() -> None:
    """

    :return:
    """
    logging.basicConfig(filename="base.log", level=logging.INFO)

    log = logging.getLogger("bot")

    uvloop.install()
    vars_json = var.Var()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(vars_json.set_var_from_file(path=os.path.abspath("config.json")))
    bot = Bot(token=vars_json.token, loop=loop,
              parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot, storage=MemoryStorage())
    dp.middleware.setup(LoggingMiddleware())
    register(dp=dp, logger=log)
    executor.start_polling(dp, on_shutdown=shutdown, loop=loop)


if __name__ == '__main__':
    set_up_app()


