# Начать обход
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from variable.var_buttons import btn_remarkNOT, btn_location, btn_cancel, btn_nextRoundName

KBremarksNOT = ReplyKeyboardMarkup(row_width=2,
    keyboard=[
        [
            KeyboardButton(text=btn_remarkNOT)
        ],
        [
            KeyboardButton(text=btn_cancel)
        ]
    ], resize_keyboard=True
)

# Клавитура для геолокации
KBget_location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=btn_location, request_location=True)
        ],
        [
            KeyboardButton(text=btn_cancel)
        ]
    ], resize_keyboard=True
)

# Клавитура закончить обход
KB_cancel = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=btn_cancel)
        ]
    ], resize_keyboard=True
)

KB_continueRound = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=btn_nextRoundName)
        ],
        [
            KeyboardButton(text=btn_cancel)
        ]
    ], resize_keyboard=True
)