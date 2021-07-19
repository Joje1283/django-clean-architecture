from abc import abstractmethod, ABC
from typing import Tuple, List, Dict, Union

from ..domain.interactors import GetRecentlyReportsInteractor, CreateReportInteractor, ReportInputBoundary, ReportOutputData, ReportInputData, ReportOutputBoundary
from ..domain.entities import Report
from ..presentation.serializers import MultipleReportsSerializer, ReportSerializer


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
    def __init__(self, get_recently_report_interactor: GetRecentlyReportsInteractor = None,
                 create_new_report_interactor: ReportInputBoundary = None,
                 create_report_presenter: ReportOutputBoundary = None):
        super().__init__()
        self.get_recently_report_interactor: GetRecentlyReportsInteractor = get_recently_report_interactor
        self.create_new_report_interactor: ReportInputBoundary = create_new_report_interactor
        self.create_report_presenter: ReportOutputBoundary = create_report_presenter

    def get(self) -> Tuple[list, int]:
        reports: List[Report] = self.get_recently_report_interactor.set_params().execute()
        body: List[Dict[str, str]] = MultipleReportsSerializer.serializer(reports)
        status: int = 200
        return body, status

    def post(self, data: str) -> Tuple[Dict[str, str], int]:
        report_input_data: ReportInputData = ReportInputData(data=data)
        reoprt_output_data: ReportOutputData = self.create_new_report_interactor.set_params(
            report_input_data=report_input_data).execute()
        body: Dict[str, str] = self.create_report_presenter.serializer(report=reoprt_output_data)
        status: int = 200
        return body, status
