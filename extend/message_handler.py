import logging

from typing import List
from aiogram import Dispatcher, types
from rust_lib.target.release import librust_lib
import cpp_impliment



async def start(message: types.Message):
    await message.answer("hello")


async def result_rust(message: types.Message):
    try:
        array: List[int] = list(map(int, message.get_args().split(" ")))
    except ValueError:
        await message.answer("send integer")
        return
    answer = librust_lib.rust_out(array)
    await message.answer(answer)


async def cpp_result(message: types.Message):
    await message.answer(cpp_impliment.cpp_implimen.hello_on_cpp())


async def all(message: types.Message):
    await message.answer("send /check arg")


def register(dp: Dispatcher, logger: logging) -> bool:
    dp.register_message_handler(callback=start, commands=["start"])
    dp.register_message_handler(callback=result_rust, commands=["check"])
    dp.register_message_handler(callback=all, text="1")
    logger.info("end reg")
    return True
