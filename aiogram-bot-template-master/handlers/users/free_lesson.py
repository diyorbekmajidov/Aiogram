from aiogram import types
from loader import dp, bot
from .start import databs
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@dp.message_handler(text='💰Bepul darslar')
async def FreeLesson(message:types.Message):
    data = databs.get_free_lesson()
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        keyboard = InlineKeyboardMarkup(row_width=5)
        text_data = ''
        k=1
        for lesson in data:
            text_data+=f'{k}. {lesson["name_uz"]}\n'
            keyboard.insert(InlineKeyboardButton(
                text=k,callback_data=k,url=lesson["link"]))
            k+=1
        await message.answer(text_data, reply_markup=keyboard)

    else:
        keyboard = InlineKeyboardMarkup(row_width=5)
        for lesson in data:
            text_data+=f'{k}. {lesson["name_ru"]}\n'
            keyboard.insert(InlineKeyboardButton(
                text=k,callback_data=k,url=lesson["link"]))
            k+=1
        await message.answer(text_data, reply_markup=keyboard)

