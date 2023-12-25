from dotenv import load_dotenv
load_dotenv()
import logging
import os
from aiogram import Bot, Dispatcher, executor
# from aiogram.dispatcher.filters import CommandStart
from aiogram import types

logging.basicConfig(level=logging.INFO)
token = os.getenv("TOKEN")
bot  = Bot(token=token, parse_mode="HTML")
db = Dispatcher(bot=bot)

db.message_handler(comands = ['start'])
async def on_start(message:type.Message):
    await message.answer(
        text = f'Salom {message.from_user.full_name}!'
    )


print(f"API Key: {token}")

if __name__ == '__main__':
    executor.start_polling(dispatcher=db)
