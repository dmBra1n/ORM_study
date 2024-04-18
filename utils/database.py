from config import settings
from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

sync_engine = create_engine(
    url=settings.psycopg_connection_url,
    echo=False
)

session_factory = sessionmaker(sync_engine)


def checking_connection_database() -> str:
    """Checking the database connection."""
    try:
        with sync_engine.connect() as conn:
            res = conn.execute(text("SELECT VERSION()"))
            success_message = (
                f"Successfully connected to the database.\n"
                f"Database version: {res.first()[0]}"
            )
            return success_message

    except Exception as error:
        error_message = f"Database connection error: {error}"
        return error_message


class Base(DeclarativeBase):
    pass


if __name__ == '__main__':
    print(checking_connection_database())
