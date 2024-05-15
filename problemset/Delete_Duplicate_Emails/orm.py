from models import PersonOrm
from sqlalchemy import delete, exists, func, select

from utils.database import Base, session_factory, sync_engine
from utils.fetch_data import fetch_data_from_sql_query


class SyncORM:
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)

    @staticmethod
    def insert_data(sql_file_path):
        try:
            with session_factory() as session:
                data = fetch_data_from_sql_query(sql_file_path)

                for row in data["data"]:
                    session.add(PersonOrm(**row))

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

    @staticmethod
    def delete_duplicate_emails():
        with session_factory() as session:
            subq = (
                select(func.min(PersonOrm.id).label("id"))
                .group_by(PersonOrm.email)
                .subquery()
            )
            query = (
                delete(PersonOrm)
                .where(~exists().where(PersonOrm.id == subq.c.id))
            )

            session.execute(query)
            session.commit()
