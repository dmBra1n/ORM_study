# import re


# def fetch_data_from_sql_query():
#     try:
#         user_id_and_time_stamp = []
#         with open("add_data.sql", "r") as file:
#             for line in file:
#                 values = re.search(r"values \('(\d+)', '(.*)'\)", line)
#                 id = int(values.group(1))
#                 email = values.group(2)
#                 user_id_and_time_stamp.append((id, email))
#
#             return user_id_and_time_stamp
#
#     except Exception as e:
#         raise Exception(f"An error occurred while fetching data from SQL query: {e}")


import re
from itertools import zip_longest


def fetch_data_from_sql_query(file_path):

    data_list = {
        "name_table": None,
        "data": []
    }

    table_pattern = r"insert into (\w+)"
    columns_pattern = r"\((.*?)\)"
    values_pattern = r"values \((.*?)\)"

    try:
        with open(file_path, "r") as file:
            for line in file:
                columns = re.search(columns_pattern, line).group(1)
                values = re.search(values_pattern, line).group(1)

                columns_list = [col.strip() for col in columns.split(',')]
                values_list = re.findall(r"'(.*?)'", values)

                columns_values = dict(zip_longest(columns_list, values_list))
                data_list["data"].append(columns_values)

            table_name = re.search(table_pattern, line).group(1)
            data_list["name_table"] = table_name.lower()

        return data_list

    except Exception as e:
        raise Exception(f"An error occurred while fetching data from SQL query: {e}")
