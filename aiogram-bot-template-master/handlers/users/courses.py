from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru, course_registration_uz,course_registaration_ru
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz

@dp.message_handler(text=["Kurslarimiz", "Наши курсы"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
    else:
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu_ru
        )

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']))
async def buying_course(call: types.CallbackQuery):
    cource = call.data
    if databs.get_user(call.from_user.id)['lang'] == "uz":
        await call.message.answer(f"Siz {cource.split(':')[1]}  Kursini tanladingiz.\nruyhatda utishni istasangiz tilfon raqam yuborish kinopkasini bosing", reply_markup=course_registration_uz)
    else:
        await call.message.answer(f"Siz {cource}  Kursini tanladingiz.", reply_markup=course_registaration_ru)

@dp.message_handler(text=['🔙 Ortga qaytish','🔙 Назад'])
async def cansel_course(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
    else:
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu_ru
        )

@dp.callback_query_handler(course_callback.filter(item_name=['cancel']))
async def cansel_menu(call: types.CallbackQuery):
    if databs.get_user(call.from_user.id)['lang'] == "uz":
        await call.message.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
    else:
        await call.message.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_ru
        )