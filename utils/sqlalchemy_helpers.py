from typing import Union

from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy.engine.result import ChunkedIteratorResult
from tabulate import tabulate


class DisplayUtils:
    """
    Utility class for displaying SQLAlchemy ORM objects and
    core query results in a tabular format.
    """

    @staticmethod
    def display_orm(result: Union[ChunkedIteratorResult, None]) -> None:
        """
        Displays the attribute values of SQLAlchemy ORM model objects in a tabular format.
        :param:  A list of SQLAlchemy ORM model objects to display.
        :return: None
        """
        if result:
            objects = result.scalars().all()
            headers = objects[0].__table__.columns.keys()
            data = [tuple(getattr(obj, attr) for attr in headers) for obj in objects]
            print(tabulate(data, headers=headers, tablefmt="psql"))
        else:
            print("No ORM objects to display")

    @staticmethod
    def display_core(result: Union[CursorResult, None]) -> None:
        """
        Displays the attribute values of SQLAlchemy core query results in a tabular format.
        :param: SQLAlchemy core query result to display.
        :return: None
        """
        if result:
            headers = result.keys()
            data = result.all()
            print(tabulate(data, headers=headers, tablefmt="psql"))
        else:
            print("No core query results to display")
