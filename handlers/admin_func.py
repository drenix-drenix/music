from pydoc import doc
from main import bot, dp
from aiogram.types import Message
from cfg import admin_id 
from keyboard import adminMenu


@dp.message_handler(text='Выгрузить')
async def load_base(message: Message):
    id = message.from_id
    if id == admin_id:
        f = open('base.db', 'rb')
        await bot.send_document(chat_id=admin_id, document=f, caption='Вот твоя ебейшая БД', reply_markup=adminMenu)
        f.close()
    else:
        await message.answer(text='Вы не администратор!')
