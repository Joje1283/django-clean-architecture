from typing import List, Dict

from ..domain.entities import Report
from ..domain.interactors import ReportOutputData, ReportOutputBoundary


class MultipleReportsSerializer:
    @staticmethod
    def serializer(reports: List) -> List[Dict[str, str]]:
        return [ReportSerializer.serializer(report) for report in reports]


class ReportSerializer:
    @staticmethod
    def serializer(report: ReportOutputData) -> Dict[str, str]:
        return {
            'id': str(report.id),
            'data': report.data
        }


class ReportPresenter(ReportOutputBoundary):
    def serializer(self, report: ReportOutputData) -> Dict[str, str]:
        return {
            'id': str(report.id),
            'data': report.data
        }