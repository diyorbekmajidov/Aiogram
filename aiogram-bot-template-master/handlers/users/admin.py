from aiogram import types
from keyboards.default.adminKeyboard import admin_kurs,admin_postButton

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
    text = course_data.items()
    t=''
    k=1
    for j in text:
        t+=f'{k}. {j[0]} : {j[1]}\n'
        k+=1
    await message.answer(f'{t}')

@dp.message_handler(text='Post yaratish')
async def Kurs_Statistika(message:types.Message):
    await message.answer('Qaysi turdagi xabar yuborishni tanlang!!!', reply_markup=admin_postButton)

@dp.message_handler(text='photo')
async def Post_rasm(message:types.Message):
    print(message)
    await message.answer('rasimni yuboring')

@dp.message_handler(content_types=types.ContentType.ANY)
async def get_file_id_p(message: types.Message):
    print(message)
    if message.photo:
        await message.reply(message.photo[-1].file_id)
    elif message.video:
        await message.reply(message.document.file_id)
    else:
        await message.answer('Salom')