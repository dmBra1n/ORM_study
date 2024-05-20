from sqlalchemy import text

from problemset.prb_196_Delete_Duplicate_Emails.models import metadata_obj
from utils.database import session_factory, sync_engine
from utils.sqlalchemy_helpers import DisplayUtils


class SyncCore:
    @staticmethod
    def create_tables():
        metadata_obj.reflect(bind=sync_engine)
        metadata_obj.drop_all(sync_engine)
        metadata_obj.create_all(sync_engine)

    @staticmethod
    def insert_data(sql_file_path):
        try:
            with (
                session_factory() as session,
                open(sql_file_path, "r") as file
            ):
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
            DisplayUtils.display_results(result)

    @staticmethod
    def delete_duplicate_emails():
        with session_factory() as session:
            query = (
                """DELETE FROM Person
                    WHERE id NOT IN(
                        SELECT MIN(id)
                        FROM Person
                        GROUP BY email);"""
            )
            session.execute(text(query))
            session.commit()
