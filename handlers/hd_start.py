from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from handlers.hd_round import btn_startRound
from keyboard.kb_start import KBstart, KBstart_not
from variable.var_text import text_start, text_startNot


# Выполнение команды /start
async def cmd_start (msg: Message):
    await msg.answer(text=text_start, parse_mode='HTML', reply_markup=KBstart)

# Реакция на кнопку "Да"
async def btn_call_yes (call: CallbackQuery):
    await call.message.delete_reply_markup()
    await btn_startRound(call.message)

# Реакция на кнопку "Нет"
async def btn_call_not (call: CallbackQuery):
    await call.message.delete_reply_markup()
    await call.message.delete()
    await call.message.answer(text=text_startNot, parse_mode='HTML', reply_markup=KBstart_not)

#Регистрация хендлеров
def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_callback_query_handler(btn_call_yes, lambda c: c.data == 'start_yes')
    dp.register_callback_query_handler(btn_call_not, lambda c: c.data == 'start_not')