from sqlalchemy import VARCHAR, Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class PersonOrm(Base):
    __tablename__ = "Person"
    personId: Mapped[PRIMARY_KEY]
    firstName: Mapped[str] = mapped_column(VARCHAR(255))
    lastName: Mapped[str] = mapped_column(VARCHAR(255))


class AddressOrm(Base):
    __tablename__ = "Address"
    addressId: Mapped[PRIMARY_KEY]
    personId: Mapped[int]
    city: Mapped[str] = mapped_column(VARCHAR(255))
    state: Mapped[str] = mapped_column(VARCHAR(255))


metadata_obj = MetaData()

person_table = Table(
    "person",
    metadata_obj,
    Column("personid", Integer, primary_key=True, autoincrement=True),
    Column("firstname", VARCHAR(255)),
    Column("lastname", VARCHAR(255))
)

address_table = Table(
    "address",
    metadata_obj,
    Column("addressid", Integer, primary_key=True, autoincrement=True),
    Column("personid", Integer),
    Column("city", VARCHAR(255)),
    Column("state", VARCHAR(255))
)
