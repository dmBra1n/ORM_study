from sqlalchemy import Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class TreeModel(Base):
    __tablename__ = "tree"
    id: Mapped[PRIMARY_KEY]
    p_id: Mapped[int] = mapped_column(nullable=True)


metadata_obj = MetaData()

tree_table = Table(
    "tree",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("p_id", Integer, nullable=True)
)
