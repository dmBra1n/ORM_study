from problemset.Delete_Duplicate_Emails.core import SyncCore
from problemset.Delete_Duplicate_Emails.orm import SyncORM


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("add_data.sql")
    SyncCore.get_all_emails()
    SyncCore.delete_duplicate_emails()
    SyncCore.get_all_emails()

    SyncORM.create_tables()
    SyncORM.insert_data("add_data.sql")
    SyncORM.get_all_emails()
    SyncORM.delete_duplicate_emails()
    SyncORM.get_all_emails()


if __name__ == '__main__':
    main()
