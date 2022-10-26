from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


download_but = KeyboardButton(text='Скачать песню')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(download_but)


song1 = KeyboardButton(text='1')
song2 = KeyboardButton(text='2')
song3 = KeyboardButton(text='3')
cencel = KeyboardButton(text='💢Отмена')

statistic = KeyboardButton(text='Статистика')
newsletter = KeyboardButton(text='Рассылка')
base = KeyboardButton(text='БД')

downBase = KeyboardButton(text='Выгрузить')
backAdmin = KeyboardButton(text='Админ меню')

baseMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(downBase, backAdmin)
adminMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(download_but, statistic, newsletter, base)
songMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(song1, song2, song3, cencel)
