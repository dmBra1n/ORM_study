from sqlalchemy import select
from utils.database import sync_engine, session_factory, Base
from models import PersonOrm

from fetch_data import fetch_data_from_sql_query


class SyncORM:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_data():
        try:
            with session_factory() as session:
                data = fetch_data_from_sql_query()
                for val in data:
                    session.add(PersonOrm(
                        id=val[0],
                        email=val[1]
                    ))
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def get_all_emails():
        with session_factory() as session:
            query = (
                select(PersonOrm)
            )
            res = session.execute(query)
            result = res.scalars().all()
            print(result)
