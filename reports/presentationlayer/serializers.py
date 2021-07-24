from typing import List, Dict

from reports.domainlayer.usecases.create_report import ReportOutputData, ReportOutputBoundary
from reports.domainlayer.usecases.get_recently_reports import MultipleReportOutputBoundary


class MultipleReportsPresenter(MultipleReportOutputBoundary):
    def serializer(self, reports: List[ReportOutputData]) -> List[Dict[str, str]]:
        return [{'id': str(report.id), 'data': report.data} for report in reports]


class ReportPresenter(ReportOutputBoundary):
    def serializer(self, report: ReportOutputData) -> Dict[str, str]:
        return {
            'id': str(report.id),
            'data': report.data
        }
