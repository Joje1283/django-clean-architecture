from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod

from reports.domain.entities import Report
from reports.domain.usecases.create_report import ReportOutputData
from reports.domain.interfaces.repository import ReportDataAccess


class GetReportsInputBoundary(ABC):
    @abstractmethod
    def set_params(self) -> GetReportsInputBoundary:
        pass

    def execute(self) -> List[ReportOutputData]:
        pass


class MultipleReportOutputBoundary(ABC):
    @abstractmethod
    def serializer(self, reports: List[ReportOutputData]) -> List[Dict[str, str]]:
        pass


class GetRecentlyReportsInteractor(GetReportsInputBoundary):
    def __init__(self, report_repo: ReportDataAccess):
        self.report_repo: ReportDataAccess = report_repo

    def set_params(self) -> GetReportsInputBoundary:
        return self

    def execute(self) -> List[ReportOutputData]:
        reports: List[Report] = self.report_repo.get_recently_reports()
        result: List[ReportOutputData] = []
        for report in reports:
            result.append(ReportOutputData(id=report.id, data=report.data))
        return result
