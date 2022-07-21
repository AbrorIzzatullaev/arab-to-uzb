import sqlite3
from keyboards.default.tugma import uz,ar,menu
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.arab_state import datas
from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher.filters import Text

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
        count = db.count_users()[0]
        msg = f"{message.from_user.get_mention(as_html=True)} bazaga qo'shildi."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except:
        pass

    await message.answer(f"Xush kelibsiz {message.from_user.full_name}!")
    await message.answer('Tilni tanlang⬇️', reply_markup=menu)      


    

@dp.message_handler(commands="count", user_id=ADMINS[0])
async def count(message: types.Message):
    await message.answer(db.count_users()[0])    


@dp.message_handler(Text(contains="#message", ignore_case=True), user_id=ADMINS[0])
async def send(message: types.Message):
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        try:
            await bot.send_message(user_id, text=f"{message.text}")     
        except:
            pass    




            