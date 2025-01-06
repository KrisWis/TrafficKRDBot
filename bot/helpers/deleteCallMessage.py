from aiogram.types import CallbackQuery
from InstanceBot import bot


async def deleteCallMessage(call: CallbackQuery):
    user_id = call.from_user.id
    message_id = call.message.message_id

    await bot.delete_message(user_id, message_id)