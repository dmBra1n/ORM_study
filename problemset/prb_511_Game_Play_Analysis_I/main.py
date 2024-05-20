from core import SyncCore
from orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_data_into_activity.sql")
    SyncCore.first_login_date()

    SyncOrm.create_tables()
    SyncOrm.insert_data("insert_data_into_activity.sql")
    SyncOrm.first_login_date()


if __name__ == '__main__':
    main()
