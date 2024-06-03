import enum
from typing import Annotated

from sqlalchemy import Column, Enum, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class Category(enum.Enum):
    Y = "Y"
    N = "N"


class ProductsOrm(Base):
    __tablename__ = "products"
    product_id: Mapped[intpk]
    low_fats: Mapped[Category]
    recyclable: Mapped[Category]


metadata_obj = MetaData()

products_table = Table(
    "products",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("low_fats", Enum(Category), nullable=False),
    Column("recyclable", Enum(Category), nullable=False)
)
