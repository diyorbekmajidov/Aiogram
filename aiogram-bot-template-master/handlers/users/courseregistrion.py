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
        await call.answer(cache_time=20)
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
            f"Ты {lang[course]} выбрали курс.\n Если хотите выиграть в списке\n Введите свое полное имя...")
        await call.answer(cache_time=20)
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
async def answer_email(message:types.Message, state: FSMContext):
    user_data = await state.get_data()
    name = message.text
    await state.update_data(
            {"name": name}
        )
    course = user_data.get("coursename").split(':')[1]
    data = databs.fillter_teacher(course)
    t=''
    teacher_keyboard = types.InlineKeyboardMarkup(row_width=5)
    for i in data:
        t+=f"{data.index(i)+1}. {i['username']}\n"
        teacher_keyboard.insert(types.InlineKeyboardButton(
                text=f"{data.index(i)+1}",callback_data=i['username']))
    if databs.get_user(message.from_user.id)['lang'] == "uz":
        await  message.answer(f"O'qituvchini tanlang\n{t}",reply_markup=teacher_keyboard)
        await Userdata.next()
    else:
        await  message.answer(f'Выбрать преподавателя\n{t}',reply_markup=teacher_keyboard)
        await Userdata.next()
@dp.callback_query_handler(state=Userdata.teacher)
async def teacher_info(call: types.CallbackQuery, state:FSMContext):
    subject = call.data
    await state.update_data(
            {"teacher": subject}
        )
    user = databs.get_user(call.from_user.id)
    if user['lang']=='uz':
        await call.message.answer("Telefon raqamini kiritish uchun tugmani bosing", reply_markup=keyboard)
        await Userdata.next()
    else:
        await call.message.answer("Нажмите кнопку, чтобы ввести номер телефона", reply_markup=keyboard)
        await Userdata.next()
    

@dp.message_handler(content_types='contact', state=Userdata.phonenumber)
async def get_contact(message: types.Message,state: FSMContext):
    data = await state.get_data()
    username = data.get("name")
    courses = data.get("coursename")
    course = courses.split(':')[1]
    teacher = data.get('teacher')
    phonenumber = message.contact.phone_number
    chat_id = message.from_user.id
    if databs.get_user_coursename(f"{chat_id}_{course}") is not None:
        databs.update_user_course(chat_id, course,username,teacher)
    # else add to user on data base
    databs.add_course_user(chat_id,username,course,phonenumber,teacher)
    if databs.get_user(chat_id)['lang'] == "uz":
        await message.answer(
            f"Rahmat, <b>{username}</b>.\n"
            f"O'qtuvchi{teacher}.\n"
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