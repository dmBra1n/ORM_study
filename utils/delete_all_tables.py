from sqlalchemy import inspect, text
from utils.database import sync_engine
from typing import List


def delete_all_tables(tables: List[str]):
    if tables:
        with sync_engine.connect() as conn:
            for table_name in tables:
                stmt = f"DROP TABLE {table_name} CASCADE;"
                conn.execute(text(stmt))
                print(f"#The {table_name} table has been DELETED.")

            conn.commit()
    else:
        print("#There are no tables in the database")


def main():
    inspector = inspect(sync_engine)
    tables = inspector.get_table_names()
    delete_all_tables(tables)


if __name__ == '__main__':
    main()
