from sqlalchemy import VARCHAR, BigInteger, Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import Base


class WorldOrm(Base):
    __tablename__ = "world"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(VARCHAR(255))
    continent: Mapped[str] = mapped_column(VARCHAR(255))
    area: Mapped[int]
    population: Mapped[int]
    gdp: Mapped[int] = mapped_column(BigInteger)


metadata_obj = MetaData()

world_table = Table(
    "world",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", VARCHAR(255)),
    Column("continent", VARCHAR(255)),
    Column("area", Integer),
    Column("population", Integer),
    Column("gdp", BigInteger)
)
