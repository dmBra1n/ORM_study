import datetime

from sqlalchemy import Column, Date, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


class ViewsOrm(Base):
    __tablename__ = "views"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    article_id: Mapped[int]
    author_id: Mapped[int]
    viewer_id: Mapped[int]
    view_date: Mapped[datetime.date]


metadata_obj = MetaData()

views_table = Table(
    "views",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("article_id", Integer),
    Column("author_id", Integer),
    Column("viewer_id", Integer),
    Column("view_date", Date)
)
