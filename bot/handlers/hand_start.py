from aiogram import types
from InstanceBot import router
from aiogram.filters import CommandStart, StateFilter
from utils import texts
from keyboards import Keyboards


# Отправка стартового меню при вводе "/start"
async def start(message: types.Message):
    await message.answer(texts.start_text, 
    reply_markup=await Keyboards.first_page_kb())


# Отправка стартового меню при нажатии кнопки "Назад"
async def back(call: types.CallbackQuery):
    await call.message.edit_text(texts.start_text, 
    reply_markup=await Keyboards.first_page_kb())


# Отправка сообщения по нажатию кнопок на первой странице
first_page_texts = {
    "price_list": texts.price_list_text, 
    "about_us": texts.about_us_text, 
    "our_socials": texts.our_contacts_text
}

async def onClick_first_page_buttons(call: types.CallbackQuery):
    text_key = call.data.split("|")[1]

    await call.message.edit_text(first_page_texts[text_key], 
    reply_markup=await Keyboards.price_list_kb() 
    if text_key == "price_list" else await Keyboards.back_to_start_menu_kb())


# Отправка сообщения по нажатию кнопок в прайс-листе
price_list_texts = {
    "socials_develop": texts.socials_develop_text, 
    "fresh_marketing": texts.fresh_marketing_text, 
    "good_websites": texts.good_websites_text, 
    "flex_bots": texts.flex_bots_text, 
    "design_and_creative": texts.design_and_creative_text, 
    "billboards_and_banners": texts.billboards_and_banners_text, 
    "traffic_tide": texts.traffic_tide_text, 
    "analytics_and_campaign": texts.analytics_and_campaign_text, 
    "meetings_and_shoots": texts.meetings_and_shoots_text, 
    "studying_and_personnel": texts.studying_and_personnel_text, 
}

async def onClick_price_list_buttons(call: types.CallbackQuery):
    text_key = call.data.split("|")[1]

    await call.message.edit_text(price_list_texts[text_key], 
    reply_markup=await Keyboards.back_to_price_list_kb())


def hand_add():
    router.message.register(start, StateFilter("*"), CommandStart())

    router.callback_query.register(back, lambda c:c.data == "back_start_menu")

    router.callback_query.register(onClick_first_page_buttons, lambda c:c.data.startswith("start"))

    router.callback_query.register(onClick_price_list_buttons, lambda c:c.data.startswith("price_list"))
