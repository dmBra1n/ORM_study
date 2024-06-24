from models import ScoresModel
from sqlalchemy import func, select, text
from sqlalchemy.orm import aliased

from utils.sqlalchemy_helpers import BaseCore, BaseOrm, DisplayUtils


class RankScoresCore(BaseCore):
    def rank_score(self):
        with self.session() as session:
            query = (
                """SELECT score,
                        DENSE_RANK() OVER(
                        ORDER BY score DESC
                        ) as "rank"
                    FROM Scores;"""
            )
            result = session.execute(text(query))
            DisplayUtils.display_results(result)


class RankScoresOrm(BaseOrm):
    def rank_score(self):
        with self.session() as session:
            scores = aliased(ScoresModel)
            query = (
                select(
                    scores.score,
                    func.dense_rank()
                    .over(order_by=scores.score.desc())
                    .label("rank")
                )
            )
            result = session.execute(query)
            DisplayUtils.display_results(result)
