from sqlalchemy import create_engine, text
from config import settings

engine_mysql = create_engine(
    url=settings.psycopg_connection_url,
    echo=False
)

with engine_mysql.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"res = {res.first()}")
