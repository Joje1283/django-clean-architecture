from typing import List
from dataclasses import dataclass

from ..domain.entities import Report
from reports.domain.usecases.create_report import ReportDataAccess
from ..repositories import ReportDatabaseRepo


@dataclass
class ReportDataAccessInputData:
    data: str


class ReportRepo(ReportDataAccess):  # Data Access -> Database
    def __init__(self, db_repo: ReportDatabaseRepo, cache_repo=None):
        self.db_repo: ReportDatabaseRepo = db_repo
        self.cache_repo = cache_repo

    def get_recently_reports(self) -> List[Report]:
        return self.db_repo.get_recently_reports()

    def create_report(self, report: Report) -> Report:
        return self.db_repo.create_report(report)
