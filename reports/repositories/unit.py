from typing import List

from ..domain.entities import Report
from ..repositories import ReportDatabaseRepo


class ReportRepo:
    def __init__(self, db_repo: ReportDatabaseRepo, cache_repo=None):
        self.db_repo: ReportDatabaseRepo = db_repo
        self.cache_repo = cache_repo

    def get_recently_reports(self) -> List[Report]:
        return self.db_repo.get_recently_reports()

    def create_report(self, report: Report) -> Report:
        return self.db_repo.create_report(report)
