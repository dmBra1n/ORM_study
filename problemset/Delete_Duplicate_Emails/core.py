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
    def insert_data():
        try:
            with session_factory() as session, open("add_data.sql", "r") as file:
                sql_queries = file.readlines()
                for query in sql_queries:
                    session.execute(text(query.strip()))
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

    @staticmethod
    def get_all_emails():
        with session_factory() as session:
            query = """SELECT * FROM Person"""
            result = session.execute(text(query))
            emails = result.all()
            print(f"emails: {emails}")

    @staticmethod
    def delete_duplicate_emails():
        with session_factory() as session:
            query = (
                """ DELETE FROM Person
                    WHERE id NOT IN(
                        SELECT MIN(id)
                        FROM Person
                        GROUP BY email);"""
            )
            session.execute(text(query))
            session.commit()
