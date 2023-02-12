from loader import dp 
from aiogram.types import Message
from data_base import insert_new_user, select_user, update_user, delete_user

@dp.message_handler(commands=['new'])
async def new(message: Message):
    user = message.text.split()[1:]
    if len(user) == 4:
        insert_new_user(tuple(user))
        await message.answer(f'Контакт {user[0]} успешно добавлен в БД')

@dp.message_handler(commands=['find'])
async def find(message: Message):
    criterion = message.text.split()[1]
    result = select_user(criterion)
    result_string = f'Результат запроса по {criterion}:\n'
    for user in result:
        result_string += f'{user[0]} ({user[1]})\n'
    await message.answer(result_string)

@dp.message_handler(commands=['change'])
async def change(message: Message):
    original = message.text.split()[1]
    new_name = message.text.split()[2]
    update_user(original, new_name)
    await message.answer(f'Контакт {original} изменён на {new_name}')

@dp.message_handler(commands=['del'])
async def change(message: Message):
    crit = message.text.split()[1]
    value = message.text.split()[2]
    delete_user(crit, value)
    await message.answer(f'Контакт {value} был удалён')