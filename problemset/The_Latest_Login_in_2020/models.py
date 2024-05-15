import datetime
from typing import Annotated

from sqlalchemy import Column, DateTime, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class LoginsOrm(Base):
    __tablename__ = "logins"

    id: Mapped[intpk]
    user_id: Mapped[int]
    time_stamp: Mapped[datetime.datetime]


metadata_obj = MetaData()

logins_table = Table(
    "logins",
    metadata_obj,
    Column("user_id", Integer),
    Column("time_stamp", DateTime)
)
