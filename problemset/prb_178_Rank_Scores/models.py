from sqlalchemy import DECIMAL, Column, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column

from utils.database import PRIMARY_KEY, Base


class ScoresModel(Base):
    __tablename__ = "scores"
    id: Mapped[PRIMARY_KEY]
    score: Mapped[int] = mapped_column(DECIMAL(3, 2))


metadata_obj = MetaData()

scores_table = Table(
    "scores",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("score", DECIMAL(3, 2))
)
