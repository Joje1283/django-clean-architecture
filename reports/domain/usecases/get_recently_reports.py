from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod

from ..entities import Report
from reports.domain.interfaces.repository import ReportDataAccess


class GetReportsInputBoundary(ABC):
    @abstractmethod
    def set_params(self) -> GetReportsInputBoundary:
        pass

    def execute(self) -> List[Report]:
        pass


class GetRecentlyReportsInteractor(GetReportsInputBoundary):
    def __init__(self, report_repo: ReportDataAccess):
        self.report_repo: ReportDataAccess = report_repo

    def set_params(self) -> GetReportsInputBoundary:
        return self

    def execute(self) -> List[Report]:
        return self.report_repo.get_recently_reports()
