from __future__ import annotations

from .entities import Report
from .repositories.unit import ReportRepo


class GetRecentlyReportsInteractor:
    def __init__(self, report_repo: ReportRepo):
        self.report_repo: ReportRepo = report_repo

    def set_params(self) -> GetRecentlyReportsInteractor:
        return self

    def execute(self) -> list:
        return self.report_repo.get_recently_reports()


class CreateReportInteractor:
    def __init__(self, report_repo: ReportRepo):
        self.report_repo: ReportRepo = report_repo

    def set_params(self, data: str) -> CreateReportInteractor:
        self.data: str = data
        return self

    def execute(self) -> Report:
        report = Report(data=self.data)
        # permission check
        # validation check
        return self.report_repo.create_report(report)
