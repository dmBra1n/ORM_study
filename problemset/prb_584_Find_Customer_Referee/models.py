from sqlalchemy import VARCHAR, Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


class CustomerOrm(Base):
    __tablename__ = "customer"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(25))
    referee_id: Mapped[int] = mapped_column(nullable=True)


metadata_obj = MetaData()

customer_table = Table(
    "customer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(25)),
    Column("referee_id", Integer, nullable=True)
)
