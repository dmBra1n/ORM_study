import datetime

from sqlalchemy import VARCHAR, Column, Date, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class DailySalesModel(Base):
    __tablename__ = "dailysales"
    id: Mapped[PRIMARY_KEY]
    date_id: Mapped[datetime.date]
    make_name: Mapped[str] = mapped_column(VARCHAR(20))
    lead_id: Mapped[int]
    partner_id: Mapped[int]


metadata_obj = MetaData()

daily_sales_table = Table(
    "dailysales",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("date_id", Date),
    Column("make_name", VARCHAR(20)),
    Column("lead_id", Integer),
    Column("partner_id", Integer)
)
