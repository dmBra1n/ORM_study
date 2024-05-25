from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import Base


class UsersOrm(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(30))

    riders: Mapped[list["RidesOrm"]] = relationship(
        back_populates="user"
    )


class RidesOrm(Base):
    __tablename__ = "rides"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"
    ))
    distance: Mapped[int]

    user: Mapped["UsersOrm"] = relationship(
        back_populates="riders"
    )


metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(30))
)

rides_table = Table(
    "rides",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE")),
    Column("distance", Integer)
)
