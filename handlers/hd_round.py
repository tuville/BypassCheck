import ast
import os

import cv2
from PIL import Image
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from pyzbar.pyzbar import decode

from config import bot, CHAT_ID
from keyboard.kb_round import KBget_location, KBremarksNOT, KB_cancel, KB_continueRound
from keyboard.kb_securityWorker import KB_workingShift, KB_securityWorker_1, KB_securityWorker_2, KB_securityWorker_3, \
    KB_securityWorker_4
from keyboard.kb_start import KBstart_not
from variable.var_buttons import btn_startRoundName, btn_cancel, btn_nextRoundName
from variable.var_qrValue import qr_value
from variable.var_text import text_name_SecWorker, text_remark, text_location, text_qrcode, text_chooseShift, \
    text_checkPoint_1, text_checkPoint_2, text_checkPoint_4, text_qrcode_2

ChatID = ast.literal_eval(CHAT_ID)
cv2_reader = cv2.QRCodeDetector()


class CheckPoint(StatesGroup):
    CP_name_SecWorker = State()  # Состояние "ФИО"
    CP_QR_data_1 = State()  # Состояние КТ №1 (значение QR-кода)
    CP_QR_data_2 = State()  # Состояние КТ №2 (значение QR-кода)
    CP_QR_data_3 = State()  # Состояние КТ №3 (значение QR-кода)
    CP_location = State()  # Состояние геопозиции
    CP_QR_data_4 = State()  # Состояние КТ №4 (значение QR-кода)
    CP_QR_data_5 = State()  # Состояние КТ №5 (значение QR-кода)
    CP_remark = State()  # Состояние замечания


# Кнопка "Отмена"
async def cmd_cancel(msg: Message, state: FSMContext):
    await msg.answer("Обход завершен!", reply_markup=KBstart_not)
    current_state = await state.get_state()

    if current_state is None:
        return
    await state.finish()


# Выбираем ФИО
async def btn_startRound(msg: Message):
    await msg.answer(text_chooseShift, reply_markup=KB_workingShift)


# Выбираем сотрудника со смены №1
async def btn_nameSecWorker_1(call: CallbackQuery):
    await CheckPoint.CP_name_SecWorker.set()
    await call.message.answer(text_name_SecWorker, reply_markup=KB_securityWorker_1)


# Выбираем сотрудника со смены №2
async def btn_nameSecWorker_2(call: CallbackQuery):
    await CheckPoint.CP_name_SecWorker.set()
    await call.message.answer(text_name_SecWorker, reply_markup=KB_securityWorker_2)


# Выбираем сотрудника со смены №3
async def btn_nameSecWorker_3(call: CallbackQuery):
    await CheckPoint.CP_name_SecWorker.set()
    await call.message.answer(text_name_SecWorker, reply_markup=KB_securityWorker_3)


# Выбираем сотрудника со смены №4
async def btn_nameSecWorker_4(call: CallbackQuery):
    await CheckPoint.CP_name_SecWorker.set()
    await call.message.answer(text_name_SecWorker, reply_markup=KB_securityWorker_4)


# Сохраняем ФИО ===> Добавляем данные по QR-коду
async def process_name_SecWorker(msg: Message, state: FSMContext):
    await state.update_data(CP_name_SecWorker=msg.text)
    await CheckPoint.next()
    await msg.answer(text_qrcode, reply_markup=KB_cancel)


# Сохраняем данные по QR-коду ===> Добавляем Геолокацию
async def process_QRdecoder_1(msg: Message, state: FSMContext):
    image_id = await bot.get_file(msg.photo[-1].file_id)  # Получаем ID изображения
    global image_time_1
    image_time_1 = msg.date
    new_image = await bot.get_file(image_id.file_id)  # Получаем ID изображения
    await new_image.download('qr.jpg')  # Скачиваем QR-код
    result = decode(Image.open('qr.jpg'))  # Открываем QR-код
    img = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)  # Считываем QR-код
    global cv2_out1
    cv2_out1 = cv2_reader.detectAndDecode(img=img)[0]  # Перекодируем QR-код
    os.remove('qr.jpg')  # Удаляем изображение с OS

    # Анализ QR-кода
    if cv2_out1 in qr_value:
        await state.update_data(CP_QR_data_1=cv2_out1)
        await CheckPoint.next()
        await msg.answer(text_checkPoint_1, reply_markup=KB_cancel)
    else:
        await msg.answer('Не, пробуй еще раз', reply_markup=KB_cancel)

async def process_QRdecoder_2(msg: Message, state: FSMContext):
    image_id = await bot.get_file(msg.photo[-1].file_id)  # Получаем ID изображения
    global image_time_2
    image_time_2 = msg.date
    new_image = await bot.get_file(image_id.file_id)  # Получаем ID изображения
    await new_image.download('qr.jpg')  # Скачиваем QR-код
    result = decode(Image.open('qr.jpg'))  # Открываем QR-код
    img = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)  # Считываем QR-код
    global cv2_out2
    cv2_out2 = cv2_reader.detectAndDecode(img=img)[0]  # Перекодируем QR-код
    os.remove('qr.jpg')  # Удаляем изображение с OS

    # Анализ QR-кода
    if cv2_out2 in qr_value:
        await state.update_data(CP_QR_data_2=cv2_out2)
        await CheckPoint.next()
        await msg.answer(text_checkPoint_2, reply_markup=KB_cancel)
    else:
        await msg.answer('Не, пробуй еще раз', reply_markup=KB_cancel)

async def process_QRdecoder_3(msg: Message, state: FSMContext):
    image_id = await bot.get_file(msg.photo[-1].file_id)  # Получаем ID изображения
    global image_time_3
    image_time_3 = msg.date
    new_image = await bot.get_file(image_id.file_id)  # Получаем ID изображения
    await new_image.download('qr.jpg')  # Скачиваем QR-код
    result = decode(Image.open('qr.jpg'))  # Открываем QR-код
    img = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)  # Считываем QR-код
    global cv2_out3
    cv2_out3 = cv2_reader.detectAndDecode(img=img)[0]  # Перекодируем QR-код
    os.remove('qr.jpg')  # Удаляем изображение с OS

    # Анализ QR-кода
    if cv2_out3 in qr_value:
        await state.update_data(CP_QR_data_3=cv2_out3)
        await CheckPoint.next()
        await msg.answer(text_location, reply_markup=KBget_location)
    else:
        await msg.answer('Не, пробуй еще раз', reply_markup=KB_cancel)

# Сохраняем геолокацию ===> Добавляем замечания
async def process_getLocation(msg: Message, state: FSMContext):
    await state.update_data(CP_location=f'Ш={msg.location.longitude}, Д={msg.location.latitude}')
    await CheckPoint.next()
    await msg.answer(text_qrcode_2, reply_markup=KB_cancel)

async def process_QRdecoder_4(msg: Message, state: FSMContext):
    image_id = await bot.get_file(msg.photo[-1].file_id)  # Получаем ID изображения
    global image_time_4
    image_time_4 = msg.date
    new_image = await bot.get_file(image_id.file_id)  # Получаем ID изображения
    await new_image.download('qr.jpg')  # Скачиваем QR-код
    result = decode(Image.open('qr.jpg'))  # Открываем QR-код
    img = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)  # Считываем QR-код
    global cv2_out4
    cv2_out4 = cv2_reader.detectAndDecode(img=img)[0]  # Перекодируем QR-код
    os.remove('qr.jpg')  # Удаляем изображение с OS

    # Анализ QR-кода
    if cv2_out4 in qr_value:
        await state.update_data(CP_QR_data_4=cv2_out4)
        await CheckPoint.next()
        await msg.answer(text_checkPoint_4, reply_markup=KB_cancel)
    else:
        await msg.answer('Не, пробуй еще раз', reply_markup=KB_cancel)


async def process_QRdecoder_5(msg: Message, state: FSMContext):
    image_id = await bot.get_file(msg.photo[-1].file_id)  # Получаем ID изображения
    global image_time_5
    image_time_5 = msg.date
    new_image = await bot.get_file(image_id.file_id)  # Получаем ID изображения
    await new_image.download('qr.jpg')  # Скачиваем QR-код
    result = decode(Image.open('qr.jpg'))  # Открываем QR-код
    img = cv2.imread('qr.jpg', cv2.IMREAD_GRAYSCALE)  # Считываем QR-код
    global cv2_out5
    cv2_out5 = cv2_reader.detectAndDecode(img=img)[0]  # Перекодируем QR-код
    os.remove('qr.jpg')  # Удаляем изображение с OS

    # Анализ QR-кода
    if cv2_out5 in qr_value:
        await state.update_data(CP_QR_data_5=cv2_out5)
        await CheckPoint.next()
        await msg.answer(text_remark, reply_markup=KBremarksNOT)
    else:
        await msg.answer('Не, пробуй еще раз', reply_markup=KB_cancel)


# Сохраняем замечания ===> Завершаем стейт и делаем репосты
async def process_remark(msg: Message, state: FSMContext):
    await state.update_data(CP_remark=msg.text)

    CheckPoint_data = await state.get_data()
    await bot.send_message(chat_id=ChatID,

                           text=f"✅ Данные по обходу. \n\n"
                                f"🟡 <b>ФИО сотрудника:</b> {CheckPoint_data['CP_name_SecWorker']}\n\n"

                                f" Контрольная точка <b>№1</b>\n"
                                f"⚽️ <b>Значение QR-кода:</b> {CheckPoint_data['CP_QR_data_1']}\n"
                                f"⚽️ <b>Время:</b> {image_time_1} \n\n"

                                f" Контрольная точка <b>№2</b>\n"
                                f"⚽️ <b>Значение QR-кода:</b> {CheckPoint_data['CP_QR_data_2']}\n"
                                f"⚽️ <b>Время:</b> {image_time_2} \n\n"

                                f" Контрольная точка <b>№3</b>\n"
                                f"⚽️ <b>Значение QR-кода:</b> {CheckPoint_data['CP_QR_data_3']}\n"
                                f"⚽️ <b>Время:</b> {image_time_3} \n\n"

                                f" Контрольная точка <b>№4</b>\n"
                                f"⚽️ <b>Значение QR-кода:</b> {CheckPoint_data['CP_QR_data_4']}\n"
                                f"⚽️ <b>Время:</b> {image_time_4} \n\n"

                                f" Контрольная точка <b>№5</b>\n"
                                f"⚽️ <b>Значение QR-кода:</b> {CheckPoint_data['CP_QR_data_5']}\n"
                                f"⚽️ <b>Время:</b> {image_time_5} \n\n"

                                f"🟡 <b>Координаты обхода:</b> \n"
                                f"     {CheckPoint_data['CP_location']}\n"
                                f"<b>Контрольные координаты:</b> \n"
                                f"     Ш=25.000000, Д=80.000000\n\n"

                                f"🟡 <b>Замечания:</b> {CheckPoint_data['CP_remark']}",
                           parse_mode='HTML')

    await state.finish()
    await msg.answer("Обход завершен!", reply_markup=KBstart_not)


async def continue_round(msg: Message):
    await btn_startRound(msg)


# Регистрация хендлеров
def register_handlers_round(dp: Dispatcher):
    dp.register_message_handler(cmd_cancel, Text(equals=btn_cancel, ignore_case=True), state=CheckPoint)
    dp.register_message_handler(btn_startRound, Text(equals=btn_startRoundName, ignore_case=True))
    dp.register_callback_query_handler(btn_nameSecWorker_1, lambda c: c.data == 'workingShift_1')
    dp.register_callback_query_handler(btn_nameSecWorker_2, lambda c: c.data == 'workingShift_2')
    dp.register_callback_query_handler(btn_nameSecWorker_3, lambda c: c.data == 'workingShift_3')
    dp.register_callback_query_handler(btn_nameSecWorker_4, lambda c: c.data == 'workingShift_4')
    dp.register_message_handler(process_name_SecWorker, state=CheckPoint.CP_name_SecWorker)
    dp.register_message_handler(process_QRdecoder_1, content_types=['photo'], state=CheckPoint.CP_QR_data_1)
    dp.register_message_handler(process_QRdecoder_2, content_types=['photo'], state=CheckPoint.CP_QR_data_2)
    dp.register_message_handler(process_QRdecoder_3, content_types=['photo'], state=CheckPoint.CP_QR_data_3)
    dp.register_message_handler(process_getLocation, content_types=['location'], state=CheckPoint.CP_location)
    dp.register_message_handler(process_QRdecoder_4, content_types=['photo'], state=CheckPoint.CP_QR_data_4)
    dp.register_message_handler(process_QRdecoder_5, content_types=['photo'], state=CheckPoint.CP_QR_data_5)
    dp.register_message_handler(process_remark, state=CheckPoint.CP_remark)
    dp.register_message_handler(continue_round, Text(equals=btn_nextRoundName, ignore_case=True))