from aiogram import types
from .start import databs
from loader import dp, bot
from keyboards.default.adminKeyboard import back_admin_keyboard, admin_kurs
from keyboards.inline.callback_data import course_callback
from keyboards.inline.kurslarkeybord import coursesMenu
from states.teacher_state import TeacherState
from aiogram.dispatcher import FSMContext
@dp.message_handler(text="O'qituvchi qo'shish",state=None)
async def AddTeacher(message: types.Message):
    await message.answer("O'qituvchini Ismi va familasini yozing",
                         reply_markup=back_admin_keyboard
                         )
    await TeacherState.name_teacher.set()

@dp.message_handler(state=TeacherState.name_teacher)
async def NameTeacher(message:types.Message,state:FSMContext):
    name = message.text
    await state.update_data({"teacher_name":name})
    await message.answer("<b>Qaysi fan o'qituvchisi tanlang</b>",reply_markup=coursesMenu)
    await TeacherState.subject_teacher.set()

@dp.callback_query_handler(course_callback.filter(item_name=['SAT', 'Umumiy matematika','Bolalar uchun matematika','Ingliz tili', 'DTM']), state=TeacherState.subject_teacher)
async def SubjectTeacher(call: types.CallbackQuery, state: FSMContext):
    data = call.data
    course = data.split(':')[1]
    name_data = await state.get_data()
    name = name_data.get('teacher_name')
    databs.add_teacher(name, course)
    await call.message.delete()
    await call.message.answer(f"<b>O'qituvchi muvaffaqiyatli qushildi</b>\nIsmi:{name}\nFani:{course}",
                               reply_markup=admin_kurs)
    await state.finish()