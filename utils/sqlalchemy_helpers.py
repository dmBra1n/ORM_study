from typing import List

from tabulate import tabulate


def display_attribute_values(objects) -> None:
    """
    Displays the attribute values of SQLAlchemy model objects in a tabular format.
    :param: A list of SQLAlchemy model objects or core query results to display.
    :return: None
    """
    if objects:
        if isinstance(objects, list):
            headers = objects[0].__table__.columns.keys()
            data = [(getattr(obj, attr) for attr in headers) for obj in objects]
        else:
            headers = objects.keys()
            data = objects.all()

        print(tabulate(data, headers=headers, tablefmt="psql"))
    else:
        print("No data to display")
