from models import TreeModel
from sqlalchemy import case, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class TreeNodeCore(BaseCore):
    def type_node(self):
        with self.session() as session:
            query = (
                """SELECT id, (
                        CASE
                        WHEN p_id IS NULL THEN 'Root'
                        WHEN id IN(SELECT p_id FROM Tree) THEN 'Inner'
                        ELSE 'Leaf'
                        END
                    ) AS type
                    FROM Tree;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class TreeNodeOrm(BaseOrm):
    def type_node(self):
        with self.session() as session:
            tree = aliased(TreeModel)
            subq = (
                select(tree.p_id)
                .subquery()
            )
            query = (
                select(
                    tree.id,
                    case(
                        (tree.p_id.is_(None), "Root"),
                        (tree.id.in_(select(subq)), "Inner"),
                        else_="Leaf"
                    ).label("type")
                )
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
