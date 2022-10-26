from aiogram import Bot, Dispatcher, executor
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from cfg import token


storage = MemoryStorage()
loop = asyncio.get_event_loop()
bot = Bot(token, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=storage)


if __name__ == "__main__":
    from allHandlers import dp
    from download_song import dp
    executor.start_polling(dp)
    