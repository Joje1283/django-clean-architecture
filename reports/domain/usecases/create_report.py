from __future__ import annotations
from typing import List, Dict
from abc import ABC, abstractmethod
from dataclasses import dataclass

from reports.domain.entities import Report
from reports.domain.interfaces.repository import ReportDataAccess
from reports.domain.interfaces.repository import ReportDataAccessInputData
from reports.domain.interfaces.repository import ReportDataAccessOutputData


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
        report_input_data: ReportInputData = report_input_data
        self.report: Report = Report(data=report_input_data.data)
        # check the validation by method of report's entity
        # ...
        return self

    def execute(self) -> ReportOutputData:
        data_access_input_data: ReportDataAccessInputData = ReportDataAccessInputData(data=self.report.data)
        # permission check
        # validation check
        report_ds_data: ReportDataAccessOutputData = self.report_repo.create_report(report=data_access_input_data)
        return ReportOutputData(id=report_ds_data.id, data=report_ds_data.data)
