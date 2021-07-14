from reports.repositories.repositories import ReportDatabaseRepo
from reports.repositories.unit import ReportRepo
from reports.interactors import CreateReportInteractor, GetRecentlyReportsInteractor
from reports.views import ReportsView


def create_report_database_repo():
    return ReportDatabaseRepo()


def create_report_repo():
    return ReportRepo(db_repo=create_report_database_repo())


def create_create_new_report_interactor():
    return CreateReportInteractor(report_repo=create_report_repo())


def create_get_recently_report_interactor():
    return GetRecentlyReportsInteractor(report_repo=create_report_repo())


def create_reports_view(request, **kwargs):
    return ReportsView(get_recently_report_interactor=create_get_recently_report_interactor(),
                       create_new_report_interactor=create_create_new_report_interactor())
