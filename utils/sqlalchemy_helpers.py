from sqlalchemy import text
from sqlalchemy.engine.cursor import ResultProxy
from tabulate import tabulate

from utils.fetch_data import fetch_data_from_sql_query


class DisplayUtils:
    """
    Utility class for displaying SQLAlchemy ORM objects and
    core query results in a tabular format.
    """

    @staticmethod
    def display_results(result: ResultProxy) -> None:
        """
        Displays the results of a SQLAlchemy query in a tabular format.

        This method expects a raw SQLAlchemy query result
        (without additional processing or formatting)
        and displays it in a tabular format using the tabulate library.

        :param: The result of a SQLAlchemy query (ResultProxy object).
        :return: None
        """
        query_result = result.all()
        if query_result:
            column_names = result.keys()
            print(tabulate(
                query_result, headers=column_names, tablefmt="psql"
            ))
        else:
            print("No objects to display")


class BaseCore:
    def __init__(self, engine, metadata, session):
        self.engine = engine
        self.metadata = metadata
        self.session = session

    def create_tables(self):
        self.metadata.reflect(bind=self.engine)
        self.metadata.drop_all(self.engine)
        self.metadata.create_all(self.engine)

    def insert_data(self, sql_file_path):
        try:
            with (
                self.session() as session,
                open(sql_file_path, "r") as file
            ):
                sql_queries = file.readlines()
                for query in sql_queries:
                    session.execute(text(query.strip()))
                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred while adding data: {e}")


class BaseOrm:
    def __init__(self, engine, base, session):
        self.engine = engine
        self.base = base
        self.session = session

    def create_tables(self):
        self.base.metadata.drop_all(self.engine)
        self.base.metadata.create_all(self.engine)

    def insert_data(self, sql_file_path, orm_class):
        try:
            with self.session() as session:
                data = fetch_data_from_sql_query(sql_file_path)
                for row in data["data"]:
                    session.add(orm_class(**row))

                session.commit()

        except Exception as e:
            session.rollback()
            print(f"An error occurred while adding data: {e}")
