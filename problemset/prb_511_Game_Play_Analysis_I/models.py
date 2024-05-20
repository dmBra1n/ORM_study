import datetime
from typing import Annotated

from sqlalchemy import Column, Date, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class ActivityOrm(Base):
    __tablename__ = "activity"

    id: Mapped[intpk]
    player_id: Mapped[int]
    device_id: Mapped[int]
    event_date: Mapped[datetime.date]
    games_played: Mapped[int]


metadata_obj = MetaData()

activity_table = Table(
    "activity",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("player_id", Integer),
    Column("device_id", Integer),
    Column("event_date", Date),
    Column("games_played", Integer),
)
