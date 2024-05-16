from models import metadata_obj
from sqlalchemy import text

from utils.database import session_factory, sync_engine


class SyncCore:
    @staticmethod
    def create_tables():
        metadata_obj.reflect(bind=sync_engine)
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)

    @staticmethod
    def insert_data(sql_file_path):
        try:
            with session_factory() as session, open(sql_file_path, "r") as file:
                sql_queries = file.readlines()
                for query in sql_queries:
                    session.execute(text(query.strip()))
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def first_login_date():
        with session_factory() as session:
            query = (
                """SELECT player_id, MIN(event_date) AS first_login 
                FROM activity
                GROUP BY player_id
                ORDER BY player_id;"""
            )
            result = session.execute(text(query))
            first_login = []

            for user_id, timestamp in result.all():
                formatted_timestamp = timestamp.strftime('%Y-%m-%d')
                first_login.append((user_id, formatted_timestamp))

            print(first_login)
