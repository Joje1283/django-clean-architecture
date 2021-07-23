from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass


@dataclass
class ReportDataAccessInputData:
    data: str


@dataclass
class ReportDataAccessOutputData:
    id: int
    data: str


class ReportDataAccess(ABC):
    @abstractmethod
    def get_recently_reports(self) -> List[ReportDataAccessOutputData]:
        pass

    @abstractmethod
    def create_report(self, report: ReportDataAccessInputData) -> ReportDataAccessOutputData:
        pass
