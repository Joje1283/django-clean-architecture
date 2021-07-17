from reports.entities import Report
from typing import List, Dict


class MultipleReportsSerializer:
    @staticmethod
    def serializer(reports: List) -> List[Dict[str, str]]:
        return [ReportSerializer.serializer(report) for report in reports]


class ReportSerializer:
    @staticmethod
    def serializer(report: Report) -> Dict[str, str]:
        return {
            'id': str(report.id),
            'data': report.data
        }
