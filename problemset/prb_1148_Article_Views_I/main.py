from models import ViewsOrm, metadata_obj
from solving import ArticleViewsCore, ArticleViewsOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = ArticleViewsCore(
        metadata=metadata_obj,
        session=session_factory,
        engine=sync_engine
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_views.sql")
    problem_core.find_authors()

    problem_orm = ArticleViewsOrm(
        base=Base,
        session=session_factory,
        engine=sync_engine
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_views.sql", ViewsOrm)
    problem_orm.find_authors()


if __name__ == '__main__':
    main()
