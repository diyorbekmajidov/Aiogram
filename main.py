from dotenv import load_dotenv
load_dotenv()
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.getenv("TOKEN")
print(API_TOKEN)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Salom! Men sizning botingizman!")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo(message: Message):
    await message.answer(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)



