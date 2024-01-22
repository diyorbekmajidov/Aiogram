from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru, keyboard
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz
from states.user_course import Userdata
from aiogram.dispatcher import FSMContext
@dp.message_handler(text=["Kurslarimiz", "Наши курсы"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
        await Userdata.courseName.set()
    else:
        await message.answer(
            text="Список курсов",
            reply_markup=coursesMenu_ru
        )
        await Userdata.courseName.set()

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']), state=Userdata.courseName)
async def buying_course(call: types.CallbackQuery, state: FSMContext):
    if databs.get_user(call.from_user.id)['lang'] == 'uz':
        course = call.data
        await state.update_data(
            {"coursename": course}
        )
        await call.message.answer(
            f"Siz {course.split(':')[1]}  Kursini tanladingiz.\nRuyhatda utishni istasangiz \nTo'liq ismingizni kiriting ...", )

        await Userdata.next()

    else:
        pass

@dp.message_handler(state=Userdata.fullname)
async def answer_email(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(
        {"name": name}
    )
    await message.answer("Telefon raqam kiriting", reply_markup=keyboard)

    await Userdata.next()

@dp.message_handler(content_types='contact', state=Userdata.phonenumber)
async def get_contact(message: types.Message,state: FSMContext):
    data = await state.get_data()
    username = data.get("name")
    courses = data.get("coursename")
    phonenumber = message.contact.phone_number
    databs.add_course_user(message.from_user.id,username,courses.split(':')[1],phonenumber)
    contact = message.contact
    await message.answer(
        f"Rahmat, <b>{contact.full_name}</b>.\n"
        f"Sizning {contact.phone_number} raqamingizni qabul qildik.\nAdminmiz siz bilan bog'lanadi.",
        reply_markup=keyboard_uz)

    await state.finish()

@dp.message_handler(text=['📢 Siznig kurslaringiz'])
async def cansel_course(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        data=databs.get_user_course(message.from_user.id)
        print(data)
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
        await state.finish()

@dp.message_handler(text=['🔙 Ortga qaytish','🔙 Назад'])
async def cansel_course(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
    else:
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
            text="Список курсов",
            reply_markup=keyboard_ru
        )