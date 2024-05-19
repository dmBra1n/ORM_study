from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from utils.config import settings

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

    except Exception as e:
        error_message = f"Database connection error: {e}"
        return error_message


class Base(DeclarativeBase):
    repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__}({', '.join(cols)})>"


if __name__ == '__main__':
    print(checking_connection_database())
