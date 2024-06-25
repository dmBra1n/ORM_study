from models import ScoresModel, metadata_obj
from solving import RankScoresCore, RankScoresOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = RankScoresCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_scores.sql")
    problem_core.rank_score()

    problem_orm = RankScoresOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_scores.sql", ScoresModel)
    problem_orm.rank_score()


if __name__ == '__main__':
    main()
