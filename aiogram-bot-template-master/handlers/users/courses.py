from aiogram import types
from loader import dp, bot
from .start import databs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu, coursesMenu_ru, keyboard
from keyboards.default.startMenuKeyboard import keyboard_ru, keyboard_uz, back_botton_uz, back_botton_ru
from states.user_course import Userdata
from aiogram.dispatcher import FSMContext
@dp.message_handler(text=["Kurslarimiz", "Наши курсы"])
async def settings_bot(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await message.answer("Another message with a new keyboard:", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(
            text="Kurslar ruyhati",
            reply_markup=coursesMenu)
        await Userdata.courseName.set()
    else:
        await message.answer("Another message with a new keyboard:", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(
            text="Список курсов",
            reply_markup=coursesMenu_ru
        )
        await Userdata.courseName.set()

@dp.callback_query_handler(course_callback.filter(item_name=['cancel']),state='*')
async def cansel_menu(call: types.CallbackQuery, state: FSMContext):
    if databs.get_user(call.from_user.id)['lang'] == "uz":
        await call.message.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
        await state.finish()
    else:
        await call.message.answer(
            text="Список курсов",
            reply_markup=keyboard_ru
        )
        await state.finish()

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']), state=Userdata.courseName)
async def buying_course(call: types.CallbackQuery, state: FSMContext):
    if databs.get_user(call.from_user.id)['lang'] == 'uz':
        course = call.data
        await state.update_data(
            {"coursename": course}
        )
        await call.message.answer(
            f"Siz {course.split(':')[1]}  Kursini tanladingiz.\nRuyhatda utishni istasangiz \nTo'liq ismingizni kiriting ...", 
            reply_markup=back_botton_uz
            )
        await Userdata.next()

    else:
        course = call.data
        lang={'SAT':'СИДЕЛ', 'Umumiy matematika':'Общая математика',
              'Bolalar uchun matematika':'Математика для детей',
              'Ingliz tili':'английский язык', 'DTM':'ДТМ'}
        await state.update_data(
            {"coursename": course}
        )
        course=course.split(':')[1]
        await call.message.answer(
            f"Ты {lang[course]} выбрали курс.\n Если хотите выиграть в списке\n Введите свое полное имя...", )
        await Userdata.next()


@dp.message_handler(text=['⬅Orqaga',"⬅Назад"],state='*')
async def back_to_menu(msg:types.Message,state:FSMContext):
    if databs.get_user(msg.from_user.id)['lang'] == "uz":
        await msg.answer(
            text="Kurslar ruyhati",
            reply_markup=keyboard_uz)
        await state.finish()
    else:
        await msg.answer(
            text="Список курсов",
            reply_markup=keyboard_ru
        )
        await state.finish()

@dp.message_handler(state=Userdata.fullname)
async def answer_email(message: types.Message, state: FSMContext):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        name = message.text
        await state.update_data(
            {"name": name}
        )
        await message.answer("Telefon raqamini kiritish uchun tugmani bosing", reply_markup=keyboard)

        await Userdata.next()
    else:
        name = message.text
        await state.update_data(
            {"name": name}
        )
        await message.answer("Нажмите кнопку, чтобы ввести номер телефона", reply_markup=keyboard)

        await Userdata.next()

@dp.message_handler(content_types='contact', state=Userdata.phonenumber)
async def get_contact(message: types.Message,state: FSMContext):
    data = await state.get_data()
    username = data.get("name")
    courses = data.get("coursename")
    course = courses.split(':')[1]
    phonenumber = message.contact.phone_number
    chat_id = message.from_user.id
    if databs.get_user_coursename(f"{chat_id}_{course}") is not None:
        databs.update_user_course(chat_id, course,username)
    # else add to user on data base
    databs.add_course_user(chat_id,username,course,phonenumber)
    if databs.get_user(chat_id)['lang'] == "uz":
        await message.answer(
            f"Rahmat, <b>{username}</b>.\n"
            f"Sizning {phonenumber} raqamingizni qabul qildik.\nAdminmiz siz bilan bog'lanadi.",
            reply_markup=keyboard_uz)
        await state.finish()
    else :
        await message.answer(
            f"Спасибо, <b>{username}</b>.\n"
            f"Мы получили ваш {phonenumber}.\n Наш администратор свяжется c вами.",
            reply_markup=keyboard_ru
        )
        await state.finish()

@dp.message_handler(text=['📢 Siznig kurslaringiz','📢 Ваши курсы:'])
async def cansel_course(message: types.Message, state=None):
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        data=databs.get_user_course(message.from_user.id)
        text=''
        if data is not None:
            for i in data:
                text +=f"\n {data.index(i)+1}.{i['course']}"
            await message.answer(
            text=f"Sizning kurslaringiz ruyhati:\n{text}",
            )
        else:
            await message.answer("<b>Siz hali bizning kurslarimizga ro'yxatdan o'tmagansiz!!!</b>")
    else:
        data=databs.get_user_course(message.from_user.id)
        text=''
        if data is not None:
            for i in data:
                text +=f"\n {data.index(i)+1}.{i['course']}"
            await message.answer(
            text=f"Sizning kurslaringiz ruyhati:\n{text}",
            )
        else:
            await message.answer('<b>Вы еще не зарегистрированы на наши курсы!!!</b>')


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