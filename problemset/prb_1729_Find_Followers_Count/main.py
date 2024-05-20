from core import SyncCore
from orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_data_into_followers.sql")
    SyncCore.followers_count()

    SyncOrm.create_tables()
    SyncOrm.insert_followers("insert_data_into_followers.sql")
    SyncOrm.followers_count()


if __name__ == '__main__':
    main()
