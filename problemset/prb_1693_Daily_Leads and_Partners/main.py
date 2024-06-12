from models import DailySalesModel, metadata_obj
from solving import DailyLeadsAndPartnersCore, DailyLeadsAndPartnersOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = DailyLeadsAndPartnersCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_dailysales.sql")
    problem_core.find_daily_lead_and_partner()

    problem_orm = DailyLeadsAndPartnersOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data(
        "insert_data_into_dailysales.sql", DailySalesModel
    )
    problem_orm.find_daily_lead_and_partner()


if __name__ == '__main__':
    main()
