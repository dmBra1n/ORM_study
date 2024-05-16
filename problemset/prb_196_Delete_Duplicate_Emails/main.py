from core import SyncCore
from orm import SyncORM


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_data_into_person.sql")
    SyncCore.get_all_emails()
    SyncCore.delete_duplicate_emails()
    SyncCore.get_all_emails()

    SyncORM.create_tables()
    SyncORM.insert_data("insert_data_into_person.sql")
    SyncORM.get_all_emails()
    SyncORM.delete_duplicate_emails()
    SyncORM.get_all_emails()


if __name__ == '__main__':
    main()
