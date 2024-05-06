from sqlalchemy import MetaData, Table, Column, Integer, VARCHAR
from typing import Annotated
from utils.database import Base
from sqlalchemy.orm import Mapped, mapped_column

intpk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]


class PersonOrm(Base):
    __tablename__ = "person"

    id: Mapped[intpk]
    email: Mapped[str]


metadata_obj = MetaData()

person_table = Table(
    "person",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("email", VARCHAR)
)
