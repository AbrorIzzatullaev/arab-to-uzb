from aiogram import types
from states.arab_state import datas
from loader import dp
from googletrans import Translator
from keyboards.default.tugma import uz, ar, menu
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

translator = Translator()


@dp.message_handler(state=datas.arab) 
async def arabian(message: types.Message, state: FSMContext):
    if message.text == "O'zbek tili":
        await state.finish()
        await message.answer("Istalgan tildan o'zbek tiliga tarjima qilishingiz mumkin.", reply_markup=ar)
        await datas.uz_state.set() 
    elif message.text == 'Menu⬅️':
        await state.finish() 
        await message.answer('Tilni tanlang⬇️', reply_markup=menu) 

    else:    
        a = translator.translate(f"{message.text}", dest='ar', src='uz').text
        b = translator.translate(f"{message.text}", dest='ar', src='uz').pronunciation
        await message.answer(f"{'<b>'}{a}{'</b>'}\n{b}", parse_mode = 'HTML')       


@dp.message_handler(state=datas.uz_state) 
async def arabian(message: types.Message, state: FSMContext): 
    if message.text == "Arab tili":
        await state.finish()
        await message.answer("Istalgan tildan arab tiliga tarjima qilishingiz mumkin.", reply_markup=uz)   
        await datas.arab.set()
    
    elif message.text == 'Menu⬅️':
        await state.finish() 
        await message.answer('Tilni tanlang⬇️', reply_markup=menu) 


    else:            
        a = translator.translate(f"{message.text}", dest='uz', src='ar').text
        await message.answer(f"{a}")    


@dp.message_handler(text='Menu⬅️')  
async def menuu(message: types.Message):
    await state.finish() 
    await message.answer('Tilni tanlang⬇️', reply_markup=menu)      



@dp.message_handler(text="Arab tili")  
async def menuu(message: types.Message):
    await message.answer("Istalgan tildan arab tiliga tarjima qilishingiz mumkin.", reply_markup=uz)   
    await datas.arab.set() 



@dp.message_handler(text="O'zbek tili")  
async def menuu(message: types.Message):  
    await message.answer("Istalgan tildan o'zbek tiliga tarjima qilishingiz mumkin.", reply_markup=ar)
    await datas.uz_state.set()  


