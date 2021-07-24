from abc import abstractmethod, ABC
from typing import Tuple, List, Dict, Union

from reports.domainlayer.usecases.create_report import CreateReportInputBoundary
from reports.domainlayer.usecases.create_report import ReportOutputData
from reports.domainlayer.usecases.create_report import ReportInputData
from reports.domainlayer.usecases.create_report import ReportOutputBoundary
from reports.domainlayer.usecases.get_recently_reports import MultipleReportOutputBoundary
from reports.domainlayer.usecases.get_recently_reports import GetReportsInputBoundary


class ViewInterface(ABC):
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def get(self, *args, **kwargs) -> Union[Tuple[list, int], Tuple[dict, int]]:
        pass

    @abstractmethod
    def post(self, *args, **kwargs) -> Union[Tuple[list, int], Tuple[dict, int]]:
        pass


class ReportsView(ViewInterface):
    def __init__(self, get_recently_report_interactor: GetReportsInputBoundary = None,
                 create_new_report_interactor: CreateReportInputBoundary = None,
                 create_report_presenter: ReportOutputBoundary = None,
                 create_multiple_report_presenter: MultipleReportOutputBoundary = None):
        super().__init__()
        self.get_recently_report_interactor: GetReportsInputBoundary = get_recently_report_interactor
        self.create_new_report_interactor: CreateReportInputBoundary = create_new_report_interactor
        self.create_report_presenter: ReportOutputBoundary = create_report_presenter
        self.create_multiple_report_presenter: MultipleReportOutputBoundary = create_multiple_report_presenter

    def get(self) -> Tuple[list, int]:
        reports: List[ReportOutputData] = self.get_recently_report_interactor.set_params().execute()
        body: List[Dict[str, str]] = self.create_multiple_report_presenter.serializer(reports=reports)
        status: int = 200
        return body, status

    def post(self, data: str) -> Tuple[Dict[str, str], int]:
        report_input_data: ReportInputData = ReportInputData(data=data)
        reoprt_output_data: ReportOutputData = self.create_new_report_interactor.set_params(
            report_input_data=report_input_data).execute()
        body: Dict[str, str] = self.create_report_presenter.serializer(report=reoprt_output_data)
        status: int = 200
        return body, status
