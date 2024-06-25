from models import TreeModel, metadata_obj
from solving import TreeNodeCore, TreeNodeOrm

from utils.database import Base, session_factory, sync_engine


def main():
    problem_core = TreeNodeCore(
        session=session_factory,
        engine=sync_engine,
        metadata=metadata_obj
    )
    problem_core.create_tables()
    problem_core.insert_data("insert_data_into_tree.sql")
    problem_core.type_node()

    problem_orm = TreeNodeOrm(
        session=session_factory,
        engine=sync_engine,
        base=Base
    )
    problem_orm.create_tables()
    problem_orm.insert_data("insert_data_into_tree.sql", TreeModel)
    problem_orm.type_node()


if __name__ == '__main__':
    main()
