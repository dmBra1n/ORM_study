from models import ActivityOrm
from sqlalchemy import func, select
from sqlalchemy.orm import aliased

from utils.database import Base, session_factory, sync_engine
from utils.fetch_data import fetch_data_from_sql_query


class SyncOrm:
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
                    session.add(ActivityOrm(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def first_login_date():
        try:
            with session_factory() as session:
                a = aliased(ActivityOrm)
                query = (
                    select(a.player_id, func.min(a.event_date).label("first_login"))
                    .group_by(a.player_id)
                    .order_by(a.player_id)
                )

                result = session.execute(query)
                first_login = []

                for user_id, timestamp in result.all():
                    formatted_timestamp = timestamp.strftime('%Y-%m-%d')
                    first_login.append((user_id, formatted_timestamp))

                print(first_login)

        except Exception as e:
            print(f"An error occurred during the database query: {e}")
