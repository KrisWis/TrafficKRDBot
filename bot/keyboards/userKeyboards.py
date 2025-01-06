from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from database.defaultValues import price_list_texts

# Реплай-клавиатура для первой страницы
async def first_page_kb():
    kb = [
        [KeyboardButton(text="💲 Прайс-лист")],
        [KeyboardButton(text="ℹ️ О нас")],
        [KeyboardButton(text="📱 Наши соц.сети")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard


# Инлайн-клавиатура для прайс-листа
async def price_list_kb():
    inline_keyboard = []

    for name, info in price_list_texts.items():
        inline_keyboard.append([InlineKeyboardButton(text=info["name"], callback_data=f"price_list|{name}")])

    inline_keyboard.append([InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_start_menu')])

    kb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    return kb


# Реплай-клавиатура для возврата в стартовое меню
async def back_kb():
    kb = [
        [KeyboardButton(text="◀️ Назад")],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard