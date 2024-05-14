from problemset.Game_Play_Analysis_I.core import SyncCore


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert._activity.sql")
    SyncCore.first_login_date()


if __name__ == '__main__':
    main()
