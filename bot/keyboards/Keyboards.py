from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Инлайн-клавиатура для первой страницы
async def first_page_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='💲 Прайс-лист', callback_data='start|price_list')],
    [InlineKeyboardButton(text='ℹ️ О нас', callback_data='start|about_us')],
    [InlineKeyboardButton(text='📱 Наши соц.сети', callback_data='start|our_socials')]])

    return kb


# Инлайн-клавиатура для прайс-листа
async def price_list_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📱 Развитие социальных сетей', callback_data='price_list|socials_develop')],
    [InlineKeyboardButton(text='📊 Свежий маркетинг', callback_data='price_list|fresh_marketing')],
    [InlineKeyboardButton(text='🌐 Продающие сайты', callback_data='price_list|good_websites')],
    [InlineKeyboardButton(text='🤖 Гибкие боты', callback_data='price_list|flex_bots')],
    [InlineKeyboardButton(text='🎨 Дизайн и креативы', callback_data='price_list|design_and_creative')],
    [InlineKeyboardButton(text='🖼 Билборды и баннеры', callback_data='price_list|billboards_and_banners')],
    [InlineKeyboardButton(text='👥 Прилив трафика', callback_data='price_list|traffic_tide')],
    [InlineKeyboardButton(text='📈 Аналитика и кампании', callback_data='price_list|analytics_and_campaign')],
    [InlineKeyboardButton(text='📹 Встречи и съёмки', callback_data='price_list|meetings_and_shoots')],
    [InlineKeyboardButton(text='📚 Обучение и персонал', callback_data='price_list|studying_and_personnel')],
    [InlineKeyboardButton(text='◀️ Назад', callback_data='back_start_menu')]])

    return kb


# Инлайн-клавиатура для возврата в стартовое меню
async def back_to_start_menu_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='◀️ Назад', callback_data='back_start_menu')]])

    return kb


# Инлайн-клавиатура для возврата в меню прайс-листа
async def back_to_price_list_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='◀️ Назад', callback_data='start|price_list')]])

    return kb