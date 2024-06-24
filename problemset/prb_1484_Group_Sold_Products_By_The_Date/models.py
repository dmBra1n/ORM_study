import datetime

from sqlalchemy import VARCHAR, Column, Date, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class ActivitiesModel(Base):
    __tablename__ = "activities"
    id: Mapped[PRIMARY_KEY]
    sell_date: Mapped[datetime.date]
    product: Mapped[str] = mapped_column(VARCHAR(20))


metadata_obj = MetaData()

activities_table = Table(
    "Activities",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sell_date", Date),
    Column("product", VARCHAR(20))
)
