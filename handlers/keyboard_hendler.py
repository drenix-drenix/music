from main import bot, dp 
from aiogram.types import Message
from keyboard import mainMenu, adminMenu, baseMenu
from cfg import admin_id


@dp.message_handler(text='💢Отмена')
async def returnMainMenu(message: Message):
    await message.answer(text='Вы перешли в главное меню', reply_markup=mainMenu)


@dp.message_handler(text='БД')
async def open_base_menu(message: Message):
    id = message.from_user.id
    if id == admin_id:
        await message.answer(text='Вы перешли в меню для работы с БД.', reply_markup=baseMenu)
    else:
        await message.answer(text='Вы не администратор!')

@dp.message_handler(text='Админ меню')
async def open_admin_menu(message: Message):
    id = message.from_user.id
    if id == admin_id:
        await message.answer(text='Вы перешли в меню администратора.', reply_markup=adminMenu)
    else:
        await message.answer(text='Вы не администратор!')
