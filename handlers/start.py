from loader import dp 
from aiogram.types import Message

@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    await message.answer(f'И тебе привет)')
