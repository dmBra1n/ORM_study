from models import LoginsOrm
from sqlalchemy import extract, func, select

from utils.database import Base, session_factory, sync_engine
from utils.fetch_data import fetch_data_from_sql_query
from utils.sqlalchemy_helpers import DisplayUtils


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
                select(
                    LoginsOrm.user_id,
                    func.max(LoginsOrm.time_stamp).label("last_stamp")
                )
                .where(extract("year", LoginsOrm.time_stamp) == 2020)
                .group_by(LoginsOrm.user_id)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
