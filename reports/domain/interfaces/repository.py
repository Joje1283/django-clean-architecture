from abc import ABC, abstractmethod
from typing import List

from reports.domain.entities import Report


class ReportDataAccess(ABC):
    @abstractmethod
    def get_recently_reports(self) -> List[Report]:
        pass

    @abstractmethod
    def create_report(self, report: Report) -> Report:
        pass
