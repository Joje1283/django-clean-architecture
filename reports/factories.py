from .presentation.serializers import ReportPresenter
from .repositories import ReportDatabaseRepo
from .repositories import ReportRepo
from .domain.interactors import CreateReportInteractor, GetRecentlyReportsInteractor
from .presentation.views import ReportsView


def create_report_database_repo() -> ReportDatabaseRepo:
    return ReportDatabaseRepo()


def create_report_repo() -> ReportRepo:
    return ReportRepo(db_repo=create_report_database_repo())


def create_create_new_report_interactor() -> CreateReportInteractor:
    return CreateReportInteractor(report_repo=create_report_repo())


def create_get_recently_report_interactor() -> GetRecentlyReportsInteractor:
    return GetRecentlyReportsInteractor(report_repo=create_report_repo())


def create_report_presenter() -> ReportPresenter:
    return ReportPresenter()


def create_reports_view(request, **kwargs) -> ReportsView:
    return ReportsView(get_recently_report_interactor=create_get_recently_report_interactor(),
                       create_new_report_interactor=create_create_new_report_interactor(),
                       create_report_presenter=create_report_presenter())
