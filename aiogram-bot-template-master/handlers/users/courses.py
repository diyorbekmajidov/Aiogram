from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru, course_registration_uz,course_registaration_ru
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz
from states.user_course import Userdata
from aiogram.dispatcher import FSMContext
@dp.message_handler(text=["Kurslarimiz", "Наши курсы"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
        await Userdata.courseName.set()
    else:
        # await message.delete()
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu_ru
        )

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']), state=Userdata.courseName)
async def buying_course(call: types.CallbackQuery, state: FSMContext):
    try:
        course = call.data
        print(call.data)
        if databs.get_user(call.from_user.id)['lang'] == "uz":
            await state.update_data({
                "corsename": course.split(':')[1]}
            )
            await call.message.answer(
                f"Siz {course.split(':')[1]}  Kursini tanladingiz.\nRuyhatda utishni istasangiz telefon raqam yuborish kinopkasini bosing", 
                reply_markup=course_registration_uz)
            await Userdata.phonenumber.set()
        else:
            await state.update_data({
                "corsename": course.split(':')[1]}
            )
            await call.message.answer(f"Siz {course}  Kursini tanladingiz.", reply_markup=course_registaration_ru)
            await Userdata.next()
    except Exception as e:
        print(e)

@dp.message_handler(state=Userdata.phonenumber)
async def anser_phonenumber(message:types.Message, state:FSMContext):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        print(message.text)
        await state.update_data(
            {"phone_number":message.text}
        )
        await message.answer("To'liq ismingizni kiriting")
        await Userdata.fullname.set()

    else:
        pass

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