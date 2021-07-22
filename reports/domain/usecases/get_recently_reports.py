from __future__ import annotations
from typing import List

from ..entities import Report
from .create_report import ReportDataAccess


class GetRecentlyReportsInteractor:
    def __init__(self, report_repo: ReportDataAccess):
        self.report_repo: ReportDataAccess = report_repo

    def set_params(self) -> GetRecentlyReportsInteractor:
        return self

    def execute(self) -> List[Report]:
        return self.report_repo.get_recently_reports()
