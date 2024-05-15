from problemset.Game_Play_Analysis_I.core import SyncCore
from problemset.Game_Play_Analysis_I.orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_activity.sql")
    SyncCore.first_login_date()

    SyncOrm.create_tables()
    SyncOrm.insert_data("insert_activity.sql")
    SyncOrm.first_login_date()


if __name__ == '__main__':
    main()
