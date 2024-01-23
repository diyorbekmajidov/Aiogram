from aiogram import types
from keyboards.default.adminKeyboard import admin_kurs

from loader import dp, bot
from .start import databs

@dp.message_handler(commands="admin")
async def admin_page(message: types.Message):
    await message.answer('admin page', reply_markup=admin_kurs)

@dp.message_handler(text='Kurslar Statistika')
async def Kurs_Statistika(message:types.Message):
    data = databs.get_user_all()
    course_data={
        'SAT':0, 
        'Umumiy matematika':0,
        'Bolalar uchun matematika':0,
        'Ingliz tili':0, 
        'DTM':0
    }
    for i in data:
        course_data[i['course']]+=1
    print(course_data)
    await message.answer('admin page')
