import datetime

from sqlalchemy import Column, Date, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


class WeatherOrm(Base):
    __tablename__ = "weather"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    recordDate: Mapped[datetime.date]
    temperature: Mapped[int]


metadata_obj = MetaData()

weather_table = Table(
    "weather",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("recorddate", Date),
    Column("temperature", Integer),
)
