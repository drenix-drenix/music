from tkinter import Menu
from main import bot, dp
from aiogram.types import Message
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from keyboard import mainMenu, songMenu, adminMenu
from downloader import find_video, download_song, pring_song_message
import os
from cfg import admin_id
from bot_funcs import update_song


class download(StatesGroup):
    name = State()
    num_song = State()

data = {}
song_names = {}
name = ''

@dp.message_handler(text='Скачать песню')
async def get_link(message: Message):
    await message.answer(text='Напиши название песни.\nНапример: Kizaru - No Stop')

    await download.name.set()

@dp.message_handler(state=download.name)
async def get_num_song(message: Message, state: FSMContext):
    global data, name, song_names
    name = message.text
    data, song_names = find_video(name)
    message_text = pring_song_message(song_names)
    
    await bot.send_message(message.from_user.id, text=message_text)

    await bot.send_message(message.from_user.id, text='Выбери номер песни', reply_markup=songMenu)
    await download.num_song.set()

@dp.message_handler(state=download.num_song)
async def go_download(message: Message, state:FSMContext):
    global data, name
    text = message.text
    id = message.from_user.id

    try:
        # option cencel
        if text == '💢Отмена':
            if id == admin_id:
                await bot.send_message(message.from_user.id, text='Вы перешли в главное меню!', reply_markup=adminMenu)
            else:
                await bot.send_message(message.from_user.id, text='Вы перешли в главное меню!', reply_markup=mainMenu)
        
        # option 1
        elif text=='1':
            video_id = data.get(text)
            await bot.send_message(message.from_user.id, text='Начинаю скачивать...')

            song = download_song(video_id=video_id, song_name=name)
            
            if id == admin_id:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=adminMenu)
            else:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=mainMenu)

            update_song(user_id=id)
            os.remove(song)        

        # option 2
        elif text=='2':
            video_id = data.get(text)
            await bot.send_message(message.from_user.id, text='Начинаю скачивать...')

            song = download_song(video_id=video_id, song_name=name)
            
            if id == admin_id:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=adminMenu)
            else:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=mainMenu)
            
            update_song(user_id=id)
            os.remove(song) 
        
        # option 3
        elif text=='3':
            video_id = data.get(text)
            await bot.send_message(message.from_user.id, text='Начинаю скачивать...')
            
            song = download_song(video_id=video_id, song_name=name)
            
            if id == admin_id:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=adminMenu)
            else:
                await bot.send_audio(message.from_user.id, open(song, "rb"), title = name, caption='Вот твоя 🎶',reply_markup=mainMenu)

            update_song(user_id=id)
            os.remove(song) 
        
        # option else if
        else:
            await bot.send_message(message.from_user.id, text='Не корректный вариант')
        
    except:
        await bot.send_message(message.from_user.id, text='Ошибка!', reply_markup=mainMenu)
    await state.finish()
