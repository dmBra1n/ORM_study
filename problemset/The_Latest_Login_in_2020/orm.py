from models import LoginsOrm
from sqlalchemy import extract, func, select

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
                    session.add(LoginsOrm(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def latest_login_in_2020():
        with session_factory() as session:
            query = (
                select(LoginsOrm.user_id, func.max(LoginsOrm.time_stamp))
                .where(extract("year", LoginsOrm.time_stamp) == 2020)
                .group_by(LoginsOrm.user_id)
            )
            result = session.execute(query)
            logins_in_2020 = []

            for user_id, timestamp in result.all():
                formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
                logins_in_2020.append((user_id, formatted_timestamp))

            print(logins_in_2020)
