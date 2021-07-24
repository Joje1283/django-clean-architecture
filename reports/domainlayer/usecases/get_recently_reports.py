from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod

from reports.domainlayer.entities import Report
from reports.domainlayer.usecases.create_report import ReportOutputData
from reports.domainlayer.interfaces.repository import ReportDataAccess
from reports.domainlayer.interfaces.repository import ReportDataAccessOutputData


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
        report_output_datas: List[ReportDataAccessOutputData] = self.report_repo.get_recently_reports()
        result: List[ReportOutputData] = []
        for output_data in report_output_datas:
            report: Report = Report(id=output_data.id, data=output_data.data)
            # check the validation by method of report's entity
            # ...
            result.append(ReportOutputData(id=report.id, data=report.data))
        return result
