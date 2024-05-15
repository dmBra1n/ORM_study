from problemset.Bank_Account_Summary_II.core import SyncCore
from problemset.Bank_Account_Summary_II.orm import SyncOrm


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_users.sql")
    SyncCore.insert_data("insert_transactions.sql")
    SyncCore.bank_account_summary()

    SyncOrm.create_tables()
    SyncOrm.insert_users("insert_users.sql")
    SyncOrm.insert_transactions("insert_transactions.sql")
    SyncOrm.bank_account_summary()


if __name__ == '__main__':
    main()
