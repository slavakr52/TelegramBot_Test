from loader import dp 
from aiogram.types import Message

@dp.message_handler(text=['run'])
async def mes_text(message: Message):
    await message.answer(f'Текст RUN принят к сведению')
