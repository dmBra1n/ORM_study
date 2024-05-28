from sqlalchemy import Column, ForeignKey, Integer, MetaData, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from utils.database import Base


class VisitsOrm(Base):
    __tablename__ = "visits"
    visit_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int]

    transactions: Mapped[list["TransactionsOrm"]] = relationship(
        back_populates="visit"
    )


class TransactionsOrm(Base):
    __tablename__ = "transactions"
    transaction_id: Mapped[int] = mapped_column(primary_key=True)
    visit_id: Mapped[int] = mapped_column(
        ForeignKey("visits.visit_id", ondelete="CASCADE")
    )
    amount: Mapped[int]

    visit: Mapped["VisitsOrm"] = relationship(
        back_populates="transactions"
    )


metadata_obj = MetaData()

visits_table = Table(
    "visits",
    metadata_obj,
    Column("visit_id", Integer, primary_key=True),
    Column("customer_id", Integer)
)

transactions_table = Table(
    "transactions",
    metadata_obj,
    Column("transaction_id", Integer, primary_key=True),
    Column(
        "visit_id", Integer, ForeignKey("visits.visit_id", ondelete="CASCADE")
    ),
    Column("amount", Integer)
)
