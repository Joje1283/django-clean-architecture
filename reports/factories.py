from reports.presentation.serializers import ReportPresenter
from reports.repositories import ReportDatabaseRepo
from reports.repositories import ReportRepo
from reports.domain.usecases.create_report import CreateReportInteractor, ReportOutputBoundary, \
    ReportInputBoundary
from reports.domain.interfaces.repository import ReportDataAccess
from reports.domain.usecases.get_recently_reports import GetRecentlyReportsInteractor
from reports.presentation.views import ReportsView, ViewInterface


def create_report_database_repo() -> ReportDatabaseRepo:
    return ReportDatabaseRepo()


def create_report_repo() -> ReportDataAccess:
    return ReportRepo(db_repo=create_report_database_repo())


def create_create_new_report_interactor() -> ReportInputBoundary:
    return CreateReportInteractor(report_repo=create_report_repo())


def create_get_recently_report_interactor() -> GetRecentlyReportsInteractor:
    return GetRecentlyReportsInteractor(report_repo=create_report_repo())


def create_report_presenter() -> ReportOutputBoundary:
    return ReportPresenter()


def create_reports_view(request, **kwargs) -> ViewInterface:
    return ReportsView(get_recently_report_interactor=create_get_recently_report_interactor(),
                       create_new_report_interactor=create_create_new_report_interactor(),
                       create_report_presenter=create_report_presenter())
