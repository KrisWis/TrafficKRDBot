from aiogram.fsm.state import State, StatesGroup


# Состояния для администратора
class AdminStates(StatesGroup):
    wait_new_priceList_item_info = State()