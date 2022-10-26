from main import bot, dp 
from aiogram import types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from cfg import admin_id
from keyboard import adminMenu
from bot_funcs import newsletter_list


class newsletter(StatesGroup):
    text = State()

@dp.message_handler(text='Рассылка')
async def start_newsletter(message: types.Message):
    id = message.from_user.id
    if id == admin_id:
        await message.answer(text='Напиши текст для рассылки или stop для отмены')
        await newsletter.text.set()

    else:
        await message.answer(text='Вы не администратор!')

@dp.message_handler(state=newsletter.text)
async def go_newsletter(message: types.Message, state: FSMContext):
    text = message.text
    users = newsletter_list()

    if text == 'stop':
        await message.answer(text='Отмена рассылки!', reply_markup=adminMenu)
    
    else:
        for user in users:
            try:
                await bot.send_message(chat_id=user, text=text)
                print(f'useru: {user} было отправленно сообщение')
            except Exception as ex:
                print(ex)
        
        await bot.send_message(chat_id=admin_id, text='Рассылка успешно завершена!', reply_markup=adminMenu)

    await state.finish()
