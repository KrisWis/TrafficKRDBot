from aiogram import types
from aiogram.fsm.context import FSMContext


# Функция для обработки и отправки медиагруппы с изображениями и видео
async def mediaGroupSend(call: types.CallbackQuery, state: FSMContext, photo_file_ids: list[str]) -> bool:
    if photo_file_ids:

        media_group_elements = []

        for photo_file_id in photo_file_ids:
            media_group_elements.append(types.InputMediaPhoto(media=photo_file_id))

        media_group_messages = await call.message.answer_media_group(media_group_elements)

        await state.update_data(media_group_messages_ids=[media_group_message.message_id for media_group_message in media_group_messages])
        
    return True