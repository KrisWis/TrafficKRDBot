from sqlalchemy import *
from database.db import Base, engine, async_session
from database.models import PriceListItemsOrm
from database.defaultValues import price_list_texts

# Создаём класс для ORM
class AsyncORM:
    # Метод для пересоздания таблиц/заполнения значениями по-умолчанию
    @staticmethod
    async def create_tables():

        async with engine.begin() as conn:
            engine.echo = False

            assert engine.url.database == 'test', 'Дропать прод запрещено'

            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            engine.echo = True
            

    '''PriceListItemsOrm'''
    # Получение пункта блока "Прайс-лист" по названию
    @staticmethod
    async def get_priceList_item_by_name(name: str) -> PriceListItemsOrm:
        async with async_session() as session:

            result = await session.execute(
                select(PriceListItemsOrm).where(PriceListItemsOrm.name == name))
            priceList_item = result.scalar()
            
            return priceList_item
        

    # Метод для заполнения таблицы прайс-листа значениями по-умолчанию
    @staticmethod
    async def fill_priceListTable_with_defaultValues():
        for name, text in price_list_texts.items():

            priceList_item = await AsyncORM.get_priceList_item_by_name(name)
            
            if not priceList_item:
                priceList_item = PriceListItemsOrm(name=name, info_text=text)

                async with async_session() as session:
                    session.add(priceList_item)

                    await session.commit() 

        return True
    '''/PriceListItemsOrm/'''    
