from models import ViewsOrm
from sqlalchemy import select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class ArticleViewsCore(BaseCore):
    def find_authors(self):
        with self.session() as session:
            query = (
                """SELECT DISTINCT author_id AS id
                FROM Views
                WHERE author_id = viewer_id
                ORDER BY 1;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class ArticleViewsOrm(BaseOrm):
    def find_authors(self):
        with self.session() as session:
            views = aliased(ViewsOrm)
            query = (
                select(views.author_id.distinct().label("id"))
                .where(views.author_id == views.viewer_id)
                .order_by(views.author_id)
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
