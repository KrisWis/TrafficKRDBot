from aiogram import types
from InstanceBot import router
from aiogram.filters import CommandStart, StateFilter
from utils import texts
from keyboards import Keyboards
from InstanceBot import bot
from aiogram.fsm.context import FSMContext
from states.User import UserStates


# Отправка стартового меню при вводе "/start"
async def start(message: types.Message, state: FSMContext):
    await message.answer(texts.start_text, 
    reply_markup=await Keyboards.first_page_kb())

    await state.clear()


# Отправка стартового меню при нажатии кнопки "Назад"
async def back(call: types.CallbackQuery,  state: FSMContext):
    user_id = call.from_user.id
    message_id = call.message.message_id
    data = await state.get_data()

    try:
        await bot.delete_message(user_id, message_id)
        await bot.delete_message(user_id, data["message_to_delete_id"])
    except: pass

    await call.message.answer(texts.start_text, 
    reply_markup=await Keyboards.first_page_kb())


# Отправка сообщения по нажатию кнопок на первой странице
first_page_texts = {
    "💲 Прайс-лист": texts.price_list_text, 
    "ℹ️ О нас": texts.about_us_text, 
    "📱 Наши соц.сети": texts.our_contacts_text
}

async def message_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    message_id = message.message_id
    text_key = message.text

    await bot.delete_message(user_id, message_id - 1)
    await bot.delete_message(user_id, message_id)

    if text_key == "◀️ Назад":
        if await state.get_state() == UserStates.from_price_list_item:
            await message.answer(texts.price_list_text, 
            reply_markup=await Keyboards.price_list_kb())

            await state.clear()
        else:
            await message.answer(texts.start_text, 
            reply_markup=await Keyboards.first_page_kb())

    else:
        message_to_delete = await message.answer(first_page_texts[text_key], 
        reply_markup=await Keyboards.price_list_kb() 
        if text_key == "💲 Прайс-лист" else await Keyboards.back_kb())

        await state.update_data(message_to_delete_id=message_to_delete.message_id)


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

async def onClick_price_list_buttons(call: types.CallbackQuery, state: FSMContext):
    text_key = call.data.split("|")[1]
    user_id = call.from_user.id
    message_id = call.message.message_id

    await bot.delete_message(user_id, message_id)

    message_to_delete = await call.message.answer(price_list_texts[text_key], 
    reply_markup=await Keyboards.back_kb())

    await state.update_data(message_to_delete_id=message_to_delete.message_id)
    await state.set_state(UserStates.from_price_list_item)


def hand_add():
    router.message.register(start, StateFilter("*"), CommandStart())

    router.message.register(message_handler)

    router.callback_query.register(back, lambda c:c.data == "back_start_menu")

    router.callback_query.register(onClick_price_list_buttons, lambda c:c.data.startswith("price_list"))
