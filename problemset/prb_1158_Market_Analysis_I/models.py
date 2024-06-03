import datetime

from sqlalchemy import (VARCHAR, Column, Date, ForeignKey, Integer, MetaData,
                        Table)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import PRIMARY_KEY, Base


class UsersOrm(Base):
    __tablename__ = "users"
    user_id: Mapped[PRIMARY_KEY]
    join_date: Mapped[datetime.date]
    favorite_brand: Mapped[str] = mapped_column(VARCHAR(10))

    orders: Mapped[list["OrdersOrm"]] = relationship(
        back_populates="user"
    )


class OrdersOrm(Base):
    __tablename__ = "orders"
    order_id: Mapped[PRIMARY_KEY]
    order_date: Mapped[datetime.date]
    item_id: Mapped[int] = mapped_column(
        ForeignKey("items.item_id", ondelete="CASCADE")
    )
    buyer_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE")
    )
    seller_id: Mapped[int]

    user: Mapped["UsersOrm"] = relationship(
        back_populates="orders"
    )
    item: Mapped["ItemsOrm"] = relationship(
        back_populates="orders"
    )


class ItemsOrm(Base):
    __tablename__ = "items"
    item_id: Mapped[PRIMARY_KEY]
    item_brand: Mapped[str] = mapped_column(VARCHAR(10))

    orders: Mapped[list["OrdersOrm"]] = relationship(
        back_populates="item"
    )


metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("user_id", Integer, primary_key=True, autoincrement=True),
    Column("join_date", Date),
    Column("favorite_brand", VARCHAR(10))
)

orders_table = Table(
    "orders",
    metadata_obj,
    Column("order_id", Integer, primary_key=True, autoincrement=True),
    Column("order_date", Date),
    Column(
        "item_id", Integer, ForeignKey("items.item_id", ondelete="CASCADE")
    ),
    Column(
        "buyer_id", Integer, ForeignKey("users.user_id", ondelete="CASCADE")
    ),
    Column("seller_id", Integer)
)

items_table = Table(
    "items",
    metadata_obj,
    Column("item_id", Integer, primary_key=True, autoincrement=True),
    Column("item_brand", VARCHAR(10))
)
