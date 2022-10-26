from main import bot, dp 
from aiogram import types
from keyboard import mainMenu, adminMenu
from bot_funcs import check_user
from cfg import admin_id


@dp.message_handler(commands='start')
async def start_func(message: types.Message):
    id = message.from_user.id
    checkUser = check_user(user_id=id)

    if id == admin_id:
        await message.answer(text='Добро пожаловать, администратор!', reply_markup=adminMenu)
    elif checkUser == 0:
        await message.answer(text=f'Привет, {message.from_user.full_name}. Добавил тебя в БД!', reply_markup=mainMenu)
        await bot.send_message(chat_id= admin_id, text=f'У вас новый пользователь, {message.from_user.username}')
    else:
        await message.answer(text=f'Привет, {message.from_user.full_name}.', reply_markup=mainMenu)
