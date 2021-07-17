from abc import abstractmethod, ABC
from typing import Tuple, List, Dict, Union

from ..domain.interactors import GetRecentlyReportsInteractor, CreateReportInteractor
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
                 create_new_report_interactor: CreateReportInteractor = None):
        super().__init__()
        self.get_recently_report_interactor: GetRecentlyReportsInteractor = get_recently_report_interactor
        self.create_new_report_interactor: CreateReportInteractor = create_new_report_interactor

    def get(self) -> Tuple[list, int]:
        reports: List[Report] = self.get_recently_report_interactor.set_params().execute()
        body: List[Dict[str, str]] = MultipleReportsSerializer.serializer(reports)
        status: int = 200
        return body, status

    def post(self, data: str) -> Tuple[dict, int]:
        report: Report = self.create_new_report_interactor.set_params(data=data).execute()
        body: Dict[str, str] = ReportSerializer.serializer(report)
        status: int = 200
        return body, status
