from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.defaultValues import price_list_texts

'''Глобальные клавиатуры для админ-меню'''
# Инлайн-клавиатура для админ-меню
async def admin_menu_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💲 Изменить текст/фото в блоке "Прайс-лист"', callback_data='admin|price_list')]])

    return kb
'''/Глобальные клавиатуры для админ-меню/'''


'''💲 Изменить текст/фото в блоке "Прайс-лист"'''
# Инлайн-клавиатура по нажатию на кнопку "💲 Изменить текст/фото в блоке "Прайс-лист""
async def change_info_in_priceList_kb():
    inline_keyboard = []

    for name, info in price_list_texts.items():
        inline_keyboard.append([InlineKeyboardButton(text=info["name"], callback_data=f"admin|change_priceList_text|{name}")])

    inline_keyboard.append([InlineKeyboardButton(text='◀️ Назад', callback_data='back_to_admin_menu')])

    kb = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

    return kb


# Инлайн-клавиатура для обработки изменения текста/фото в блоке "Прайс-лист"
async def change_info_in_priceListItem_kb(name: str):
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Изменить текст/фото', callback_data=f"admin|change_priceList_text|{name}|change")],
    [InlineKeyboardButton(text='◀️ Назад', callback_data='admin|price_list')]])

    return kb


# Инлайн-клавиатура для возврата в меню выбора пункта для изменения в нём текста/фото
async def back_to_priceListCatalog_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='◀️ Назад', callback_data='admin|price_list')]])

    return kb
'''/💲 Изменить текст/фото в блоке "Прайс-лист"/'''