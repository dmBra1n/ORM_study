from core import SyncCore
from orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_data_into_users.sql")
    SyncCore.insert_data("insert_data_into_transactions.sql")
    SyncCore.bank_account_summary()

    SyncOrm.create_tables()
    SyncOrm.insert_users("insert_data_into_users.sql")
    SyncOrm.insert_transactions("insert_data_into_transactions.sql")
    SyncOrm.bank_account_summary()


if __name__ == '__main__':
    main()
