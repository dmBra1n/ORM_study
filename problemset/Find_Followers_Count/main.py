from problemset.Find_Followers_Count.core import SyncCore
from problemset.Find_Followers_Count.orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_followers.sql")
    SyncCore.followers_count()

    SyncOrm.create_tables()
    SyncOrm.insert_followers("insert_followers.sql")
    SyncOrm.followers_count()


if __name__ == '__main__':
    main()
