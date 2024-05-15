from problemset.The_Latest_Login_in_2020.core import SyncCore
from problemset.The_Latest_Login_in_2020.orm import SyncORM


def main():
    SyncCore.create_tables()
    SyncCore.insert_data('insert_logins.sql')
    SyncCore.latest_login_in_2020()

    SyncORM.create_tables()
    SyncORM.insert_data('insert_logins.sql')
    SyncORM.latest_login_in_2020()


if __name__ == '__main__':
    main()
