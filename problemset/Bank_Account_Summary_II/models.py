from sqlalchemy import Column, MetaData, Integer, Table, VARCHAR, DateTime, ForeignKey

metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("account", Integer, primary_key=True),
    Column("name", VARCHAR)
)

transactions_table = Table(
    "transactions",
    metadata_obj,
    Column("trans_id", Integer, primary_key=True),
    Column("account", ForeignKey("users.account", ondelete="CASCADE")),
    Column("amount", Integer),
    Column("transacted_on", DateTime)
)
