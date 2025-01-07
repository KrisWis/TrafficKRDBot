from aiogram import types
from InstanceBot import router
from aiogram.filters import Command, StateFilter
from utils import adminTexts, globalTexts
from keyboards import adminKeyboards
from aiogram.fsm.context import FSMContext
from database.orm import AsyncORM
import re
from states.Admin import AdminStates
from helpers import albumInfoProcess, sendPriceListItemInfo, deleteCallMessage
from database.defaultValues import price_list_texts
from RunBot import logger
from Config import admins


'''Глобальные хендлеры для админ-меню'''
# Отправка админ-меню при вводе "/admin"
async def admin(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if user_id in admins:
        await message.answer(adminTexts.admin_start_text, 
        reply_markup=await adminKeyboards.admin_menu_kb())
    else:
        await message.answer(globalTexts.rightsError_text)

    await state.clear()


# Отправка админ-меню при нажатии кнопки "Назад"
async def back_to_admin_menu(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text(adminTexts.admin_start_text, 
    reply_markup=await adminKeyboards.admin_menu_kb())

    await state.clear()


# Отправка сообщения по нажатию на кнопки в админ-меню
async def onClick_adminMenu_buttons(call: types.CallbackQuery):
    temp = call.data.split("|")

    if temp[1] == "price_list":
        await deleteCallMessage(call)

        await call.message.answer(adminTexts.admin_priceList_choose_text, 
        reply_markup=await adminKeyboards.change_info_in_priceList_kb())
'''/Глобальные хендлеры для админ-меню/'''


'''💲 Изменить текст/фото в блоке "Прайс-лист"'''
# Отправка сообщения по нажатию пунктов в блоке "💲 Изменить текст/фото в блоке "Прайс-лист""
async def onClick_adminMenu_priceList_buttons(call: types.CallbackQuery, state: FSMContext):
    price_list_item_name = call.data.split("|")[2]

    await sendPriceListItemInfo(call, state, price_list_item_name, await adminKeyboards.change_info_in_priceListItem_kb(price_list_item_name))


# Отправка сообщения по нажатию кнопки "Изменить текст/фото" у пункта в блоке "Прайс-лист"
async def onClick_change_priceList_button(call: types.CallbackQuery, state: FSMContext):
    temp = call.data.split("|")
    await call.message.answer(adminTexts.admin_send_new_priceList_item_info)

    await state.update_data(price_list_item_name=temp[2])

    await state.set_state(AdminStates.wait_new_priceList_item_info)


# Ожидание новой информации от администратора для пункта в блоке "Прайс-лист". Изменение данных в базе данных.
async def wait_new_priceList_item_info(message: types.Message, album: list[types.Message] = [], state: FSMContext = None):
    result = await albumInfoProcess(AdminStates.wait_new_priceList_item_info, state, message, album)

    if not result:
        return

    user_text = result[0]
    photo_file_ids = result[1]
    data = await state.get_data()

    price_list_item_name = data["price_list_item_name"]

    try:
        await AsyncORM.change_priceList_item_info(price_list_item_name, user_text, photo_file_ids)

        price_list_item = await AsyncORM.get_priceList_item_by_name(price_list_item_name)

        await message.answer(adminTexts.change_priceList_item_info_success_text.format(price_list_texts[price_list_item.name]["name"]),
        reply_markup=await adminKeyboards.back_to_priceListCatalog_kb())

    except Exception as e:
        await logger.info(f"Ошибка при изменении информации пункта {price_list_item_name}: {e}")
        await message.answer(adminTexts.change_priceList_item_info_error_text)

    await state.clear()
'''/💲 Изменить текст/фото в блоке "Прайс-лист"/'''


def hand_add():
    '''Глобальные хендлеры для админ-меню'''
    router.message.register(admin, StateFilter("*"), Command("admin"))

    router.callback_query.register(back_to_admin_menu, lambda c:c.data == "back_to_admin_menu")
    
    router.callback_query.register(onClick_adminMenu_buttons, lambda c: c.data == "admin|price_list")
    '''/Глобальные хендлеры для админ-меню/'''

    '''💲 Изменить текст/фото в блоке "Прайс-лист"'''
    router.callback_query.register(onClick_adminMenu_priceList_buttons, 
    lambda c: re.match(r'^(?!.*\|change$).*\b(admin|change_priceList_text|[^|]+)\b', c.data))

    router.callback_query.register(onClick_change_priceList_button, 
    lambda c: re.match(r'\b(admin|change_priceList_text|[^|]+|change)\b', c.data))

    router.message.register(wait_new_priceList_item_info, StateFilter(AdminStates.wait_new_priceList_item_info))    
    '''/💲 Изменить текст/фото в блоке "Прайс-лист"/'''