from sqlalchemy import *
from sqlalchemy.orm import Mapped, mapped_column
from database.db import Base


# Таблица с данными пунктов в "Прайс-лист"
class PriceListItemsOrm(Base):
    __tablename__ = "priceListItems"
    
    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String())
    info_text: Mapped[str] = mapped_column(String())
    photo_file_ids: Mapped[list[str]] = mapped_column(ARRAY(String()))

    __table_args__ = (
        UniqueConstraint('id', name='unique_item'),
    )
