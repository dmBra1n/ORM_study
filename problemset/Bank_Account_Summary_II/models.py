import datetime

from sqlalchemy import (VARCHAR, Column, DateTime, ForeignKey, Integer,
                        MetaData, Table)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import Base


class UsersOrm(Base):
    __tablename__ = "users"
    account: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    transactions: Mapped[list["TransactionsOrm"]] = relationship(
        back_populates="user"
    )


class TransactionsOrm(Base):
    __tablename__ = "transactions"

    trans_id: Mapped[int] = mapped_column(primary_key=True)
    account: Mapped[int] = mapped_column(ForeignKey(
        "users.account", ondelete="CASCADE"
    ))
    amount: Mapped[int]
    transacted_on: Mapped[datetime.datetime]

    user: Mapped["UsersOrm"] = relationship(
        back_populates="transactions"
    )


metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("account", Integer, primary_key=True),
    Column("name", VARCHAR)
)

transactions_table = Table(
    "transactions",
    metadata_obj,
    Column("trans_id", Integer, primary_key=True),
    Column("account", ForeignKey("users.account", ondelete="CASCADE")),
    Column("amount", Integer),
    Column("transacted_on", DateTime)
)
