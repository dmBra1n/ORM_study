from sqlalchemy import MetaData, Table, Column, Integer, DateTime
import datetime
from typing import Annotated
from utils.database import Base
from sqlalchemy.orm import Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class LoginsOrm(Base):
    __tablename__ = "logins"

    id: Mapped[intpk]
    user_id: Mapped[int]
    time_stamp: Mapped[datetime.datetime]


metadata_obj = MetaData()

login_table = Table(
    "logins",
    metadata_obj,
    Column("user_id", Integer),
    Column("time_stamp", DateTime)
)
