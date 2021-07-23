from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod
from dataclasses import dataclass

from reports.domain.entities import Report
from reports.domain.interfaces.repository import ReportDataAccess


@dataclass
class ReportInputData:
    data: str


@dataclass
class ReportOutputData:
    id: int
    data: str


class CreateReportInputBoundary(ABC):
    @abstractmethod
    def set_params(self, report_input_data: ReportInputData) -> CreateReportInputBoundary:
        pass

    def execute(self) -> ReportOutputData:
        pass


class ReportOutputBoundary(ABC):
    @abstractmethod
    def serializer(self, report: ReportOutputData) -> Dict[str, str]:
        pass


class CreateReportInteractor(CreateReportInputBoundary):
    def __init__(self, report_repo: ReportDataAccess):
        self.report_repo: ReportDataAccess = report_repo

    def set_params(self, report_input_data: ReportInputData) -> CreateReportInputBoundary:
        self.report_input_data: ReportInputData = report_input_data
        return self

    def execute(self) -> ReportOutputData:
        report: Report = Report(data=self.report_input_data.data)
        # permission check
        # validation check
        report_ds_data: Report = self.report_repo.create_report(report)

        return ReportOutputData(id=report_ds_data.id, data=report_ds_data.data)
