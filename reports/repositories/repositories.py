from typing import List

from reports.models import Report as ORMReport
from reports.domain.entities import Report
from reports.domain.interfaces.repository import ReportDataAccessInputData
from reports.domain.interfaces.repository import ReportDataAccessOutputData


class ReportDatabaseRepo:
    @classmethod
    def get_recently_reports(cls) -> List[ReportDataAccessOutputData]:
        orm_reports = ORMReport.objects.order_by('-pk')[:10]
        reports = []
        for orm_report in orm_reports:
            reports.append(cls._decode_orm_report(orm_report))
        return reports

    @classmethod
    def create_report(cls, report: ReportDataAccessInputData) -> ReportDataAccessOutputData:
        created_orm_report = ORMReport.objects.create(data=report.data)
        return cls._decode_orm_report(created_orm_report)

    @staticmethod
    def _decode_orm_report(orm_report: ORMReport) -> ReportDataAccessOutputData:
        report = Report(id=orm_report.id, data=orm_report.data)
        return ReportDataAccessOutputData(id=orm_report.id, data=orm_report.data)
