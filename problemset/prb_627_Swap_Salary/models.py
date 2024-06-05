import enum

from sqlalchemy import VARCHAR, Column, Enum, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class Sex(enum.Enum):
    m = "m"
    f = "f"


class SalaryOrm(Base):
    __tablename__ = "salary"
    id: Mapped[PRIMARY_KEY]
    name: Mapped[str] = mapped_column(VARCHAR(100))
    sex: Mapped[Sex]
    salary: Mapped[int]


metadata_obj = MetaData()

salary_table = Table(
    "salary",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(100)),
    Column("sex", Enum(Sex)),
    Column("salary", Integer)
)
