from typing import List

from reports.domain.interfaces.repository import ReportDataAccess
from reports.domain.interfaces.repository import ReportDataAccessInputData
from reports.domain.interfaces.repository import ReportDataAccessOutputData

from reports.repositories import ReportDatabaseRepo


class ReportRepo(ReportDataAccess):  # Data Access -> Database
    def __init__(self, db_repo: ReportDatabaseRepo, cache_repo=None):
        self.db_repo: ReportDatabaseRepo = db_repo
        self.cache_repo = cache_repo

    def get_recently_reports(self) -> List[ReportDataAccessOutputData]:
        return self.db_repo.get_recently_reports()

    def create_report(self, report: ReportDataAccessInputData) -> ReportDataAccessOutputData:
        return self.db_repo.create_report(report)
