from sqlalchemy.engine.cursor import ResultProxy
from tabulate import tabulate


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
