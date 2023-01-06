import logging

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

storage = MemoryStorage()

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
CHAT_ID = os.getenv('CHAT_ID')


bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp: Dispatcher = Dispatcher(bot, storage=storage)