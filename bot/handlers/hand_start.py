from aiogram import types
from InstanceBot import router
from aiogram.filters import CommandStart, StateFilter
from utils import userTexts
from keyboards import userKeyboards
from InstanceBot import bot
from aiogram.fsm.context import FSMContext
from states.User import UserStates
from helpers import deleteCallMessage, sendPriceListItemInfo


# Отправка стартового меню при вводе "/start"
async def start(message: types.Message, state: FSMContext):
    await message.answer(userTexts.start_text, 
    reply_markup=await userKeyboards.first_page_kb())

    await state.clear()


# Отправка стартового меню при нажатии кнопки "Назад"
async def back_to_start_menu(call: types.CallbackQuery,  state: FSMContext):
    user_id = call.from_user.id
    data = await state.get_data()

    try:
        await deleteCallMessage(call)
        await bot.delete_message(user_id, data["message_to_delete_id"])
    except: pass

    await call.message.answer(userTexts.start_text, 
    reply_markup=await userKeyboards.first_page_kb())


# Отправка сообщения по нажатию кнопок на первой странице
first_page_texts = {
    "💲 Прайс-лист": userTexts.price_list_text, 
    "ℹ️ О нас": userTexts.about_us_text, 
    "📱 Наши соц.сети": userTexts.our_contacts_text
}

async def reply_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    message_id = message.message_id
    text_key = message.text

    try:
        await bot.delete_message(user_id, message_id - 1)
        await bot.delete_message(user_id, message_id)
    except: pass

    data = await state.get_data()

    if text_key == "◀️ Назад":
        if "media_group_messages_ids" in data:
            media_group_messages_ids: list[int] = data["media_group_messages_ids"]

            for media_group_message_id in media_group_messages_ids:
                await bot.delete_message(user_id, media_group_message_id)

        if await state.get_state() == UserStates.from_price_list_item:
            await message.answer(userTexts.price_list_text, 
            reply_markup=await userKeyboards.price_list_kb())

            await state.clear()
        else:
            await message.answer(userTexts.start_text, 
            reply_markup=await userKeyboards.first_page_kb())

    else:

        if text_key == "ℹ️ О нас":

            about_us_gif_id = "CgACAgIAAxkBAAIB3Wd7-9WLlC0sqQnIZ8G3cEds7RfpAAIrZwACv73gS5nfE8-wA5clNgQ"

            message_to_delete = await message.answer_animation(
            animation=about_us_gif_id,
            caption=first_page_texts[text_key], 
            reply_markup=await userKeyboards.back_kb())
        else:
            message_to_delete = await message.answer(first_page_texts[text_key], 
            reply_markup=await userKeyboards.price_list_kb() 
            if text_key == "💲 Прайс-лист" else await userKeyboards.back_kb(), disable_web_page_preview=True)

        await state.update_data(message_to_delete_id=message_to_delete.message_id)


# Отправка сообщения по нажатию кнопок в прайс-листе
async def onClick_price_list_buttons(call: types.CallbackQuery, state: FSMContext):
    price_list_item_name = call.data.split("|")[1]

    message_to_delete = await sendPriceListItemInfo(call, state, price_list_item_name, await userKeyboards.back_kb())

    await state.update_data(message_to_delete_id=message_to_delete.message_id)
    await state.set_state(UserStates.from_price_list_item)


def hand_add():
    router.message.register(start, StateFilter("*"), CommandStart())

    router.callback_query.register(back_to_start_menu, lambda c:c.data == "back_to_start_menu")

    router.callback_query.register(onClick_price_list_buttons, lambda c:c.data.startswith("price_list"))
    
    router.message.register(reply_handler, 
    lambda m:m.text in first_page_texts.keys() or m.text == "◀️ Назад")
