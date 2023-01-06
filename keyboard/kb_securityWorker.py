from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from variable.var_buttons import btn_workingShift_1, btn_workingShift_2, btn_workingShift_3, btn_workingShift_4
from variable.var_securityWorker import list_securityWorker_1, list_securityWorker_2, list_securityWorker_3, list_securityWorker_4

# Смена №1
KB_securityWorker_1 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_securityWorker_1.add(*list_securityWorker_1)

# Смена №2
KB_securityWorker_2 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_securityWorker_2.add(*list_securityWorker_2)

# Смена №3
KB_securityWorker_3 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_securityWorker_3.add(*list_securityWorker_3)

# Смена №4
KB_securityWorker_4 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
KB_securityWorker_4.add(*list_securityWorker_4)

KB_workingShift = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=btn_workingShift_1,
                                 callback_data='workingShift_1'),
            InlineKeyboardButton(text=btn_workingShift_2,
                                 callback_data='workingShift_2')
        ],
        [
            InlineKeyboardButton(text=btn_workingShift_3,
                                 callback_data='workingShift_3'),
            InlineKeyboardButton(text=btn_workingShift_4,
                                 callback_data='workingShift_4')
        ],
    ]
)

