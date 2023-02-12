from loader import dp 
from aiogram.types import Message

@dp.message_handler()
async def mes_all(message: Message):
    
    await message.answer(f'{message.from_user.first_name}, смотри чё поймал: {message.text}')