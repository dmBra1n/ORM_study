import re
from itertools import zip_longest
from typing import List


def extract_columns(line: str) -> List[str]:
    """
    Extracts column names from an SQL query line enclosed in parentheses.
    :param: A line from an SQL query.
    :return: A list of column names extracted from the line.
    """
    columns_pattern = r"\((.*?)\)"
    columns_match = re.search(columns_pattern, line)
    if columns_match:
        columns = columns_match.group(1)
        return [col.strip() for col in columns.split(',')]
    else:
        raise ValueError(
            "The string does not contain the expected values in parentheses"
        )


def extract_values(line: str) -> List[any]:
    """
    Extracts values from an SQL query line enclosed in parentheses.
    :param: A line from an SQL query.
    :return: A list of values extracted from the line.
    """
    values_pattern = r"values \((.*?)\)"
    values_match = re.search(values_pattern, line)
    if values_match:
        values = values_match.group(1)
        values_list = re.findall(r"'(.*?)'", values)
        return [int(val) if val.isdigit() else val for val in values_list]
    else:
        raise ValueError(
            "The string does not contain the expected values in parentheses"
        )


def fetch_data_from_sql_query(file_path: str) -> dict:
    """
    Fetches data from an SQL query file, extracting columns and values.
    :param: Path to the SQL query file.
    :return: A dictionary containing the table name and
    data extracted from the SQL query.
    """
    extracted_data = {
        "name_table": None,
        "data": []
    }

    table_pattern = r"insert into (\w+)"

    try:
        with open(file_path, "r") as file:
            for line in file:
                columns = extract_columns(line)
                values = extract_values(line)

                columns_values = dict(zip_longest(columns, values))
                extracted_data["data"].append(columns_values)

            table_name = re.search(table_pattern, line).group(1)
            extracted_data["name_table"] = table_name.lower()

        return extracted_data

    except Exception as e:
        raise Exception(
            f"An error occurred while fetching data from SQL query: {e}"
        )
