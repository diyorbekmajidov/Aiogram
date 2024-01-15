from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.kurslarkeybord import coursesMenu

@dp.message_handler(text=["Kurslarimiz", "Kurslarimiz"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=coursesMenu
        )
    else:
        await message.answer(
            text="⚙️ Sozlamalar!!!",
            reply_markup=settings_keyboard_ru
        )