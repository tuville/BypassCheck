from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from variable.var_buttons import btn_startYES, btn_startNOT, btn_startRoundName

# Меню при запуске программы
KBstart = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text=btn_startYES,
                                 callback_data='start_yes')
        ],
        [
            InlineKeyboardButton(text=btn_startNOT,
                                 callback_data='start_not')
        ]
    ]
)

# Меню, когда нажали "Нет"
KBstart_not = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=btn_startRoundName)
        ]
    ], resize_keyboard=True
)