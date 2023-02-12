from loader import dp 
from aiogram.types import Message
from keyboards import kb_help

@dp.message_handler(commands=['help'])
async def mes_help(message: Message):
    await message.answer('Хелп, ай нид сомбади ХЕЛБ', reply_markup=kb_help)
