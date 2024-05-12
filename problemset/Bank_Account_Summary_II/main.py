from problemset.Bank_Account_Summary_II.core import SyncCore


def main():
    SyncCore.create_tables()
    SyncCore.insert_data("insert_users.sql")
    SyncCore.insert_data("insert_transactions.sql")
    SyncCore.bank_account_summary()


if __name__ == '__main__':
    main()