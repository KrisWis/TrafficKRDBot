from aiogram.types import CallbackQuery
from helpers import mediaGroupSend, deleteCallMessage
from database.orm import AsyncORM
from utils import globalTexts
from aiogram import types
from aiogram.fsm.context import FSMContext


async def sendPriceListItemInfo(call: CallbackQuery, state: FSMContext, price_list_item_name: str, reply_markup: types.InlineKeyboardMarkup) -> types.Message:
    await deleteCallMessage(call)

    price_list_item = await AsyncORM.get_priceList_item_by_name(price_list_item_name)

    if not price_list_item: 
        await call.message.answer(globalTexts.data_notFound_text)
        return
    
    if len(price_list_item.photo_file_ids) > 1:
        await mediaGroupSend(call, state, price_list_item.photo_file_ids)

    if len(price_list_item.photo_file_ids) == 1:
        message_to_delete = await call.message.answer_photo(
        caption=globalTexts.priceList_item_infoText_isNotFound if not price_list_item.info_text else price_list_item.info_text, 
        photo=price_list_item.photo_file_ids[0], 
        reply_markup=reply_markup)
    else:
        message_to_delete = await call.message.answer(
        globalTexts.priceList_item_infoText_isNotFound if not price_list_item.info_text else price_list_item.info_text, 
        reply_markup=reply_markup)

    return message_to_delete