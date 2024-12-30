from aiogram.fsm.state import State, StatesGroup


# Состояния для пользователя
class UserStates(StatesGroup):
    from_price_list_item = State()