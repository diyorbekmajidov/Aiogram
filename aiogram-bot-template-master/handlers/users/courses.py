from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru

@dp.message_handler(text=["Kurslarimiz", "Kurslarimiz"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu
        )
        await message.answer(cache_time=60)
    else:
        await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu_ru
        )
        await message.answer(cache_time=60)