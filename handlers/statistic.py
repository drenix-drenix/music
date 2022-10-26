from main import bot, dp 
from aiogram import types
from bot_funcs import get_stat


@dp.message_handler(text='Статистика')
async def send_statistic(message: types.Message):
    id = message.from_user.id 
    songs = get_stat(user_id=id)
    message_text = f"Скачаных вами песен: <b>{songs}</b>"
    
    await message.answer(text=message_text)
