import enum

from sqlalchemy import VARCHAR, Column, Enum, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class Operation(enum.Enum):
    Buy = "Buy"
    Sell = "Sell"


class StocksOrm(Base):
    __tablename__ = "stocks"
    id: Mapped[PRIMARY_KEY]
    stock_name: Mapped[str] = mapped_column(VARCHAR(15))
    operation: Mapped[Operation]
    operation_day: Mapped[int]
    price: Mapped[int]


metadata_obj = MetaData()

stocks_table = Table(
    "stocks",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("stock_name", VARCHAR(15)),
    Column("operation", Enum(Operation)),
    Column("operation_day", Integer),
    Column("price", Integer)
)
