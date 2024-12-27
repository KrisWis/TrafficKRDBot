from aiogram import types
from InstanceBot import router
from aiogram.filters import CommandStart, StateFilter
from utils import globalTexts, userPreviousConcertsTexts, userFutureConcertsTexts, userAboutUsTexts, userWhatsNewTexts, userDiscountsTexts, userPartnersTexts
from keyboards import globalKeyboards
from database.orm import AsyncORM
from aiogram.fsm.context import FSMContext
import datetime
from InstanceBot import bot
from helpers import mediaGroupSend, sendPaginationMessage, deleteSendedMediaGroup, deleteMessage
import re


# Отправка стартового меню при вводе "/start"
async def start(message: types.Message, state: FSMContext):
    await message.answer(1)


def hand_add():
    router.message.register(start, StateFilter("*"), CommandStart())
