from django.db.models import F

from reports.models import Report as ORMReport
from reports.entities import Report


class ReportDatabaseRepo:
    @classmethod
    def get_recently_reports(cls):
        orm_reports = ORMReport.objects.order_by('-pk')[:10]
        reports = []
        for orm_report in orm_reports:
            reports.append(cls._decode_orm_report(orm_report))
        return reports

    @classmethod
    def create_report(cls, report):
        created_orm_report = ORMReport.objects.create(data=report.data)
        return cls._decode_orm_report(created_orm_report)

    @staticmethod
    def _decode_orm_report(orm_report):
        return Report(id=orm_report.id, data=orm_report.data)