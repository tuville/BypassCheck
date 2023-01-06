from aiogram.utils import executor
from config import dp

from handlers import hd_start, hd_round

async def on_statUp (_):
    print("Бот ЗАПУЩЕН и находится в СЕТИ")

hd_start.register_handlers_start(dp)
hd_round.register_handlers_round(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_statUp)