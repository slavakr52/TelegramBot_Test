from aiogram import executor
from handlers import dp
from data_base import create_table

async def on_start(_):
    try:
        create_table()
        print('DB connected... OK!')
        print('Бот запущен')
    except:
        print('DB connected... FAILURE')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup = on_start)   
