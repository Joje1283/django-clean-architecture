from .serializers import MultipleReportsSerializer, ReportSerializer


class ReportsView:
    def __init__(self, get_recently_report_interactor=None, create_new_report_interactor=None):
        self.get_recently_report_interactor = get_recently_report_interactor
        self.create_new_report_interactor = create_new_report_interactor

    def get(self):
        reports = self.get_recently_report_interactor.set_params().execute()
        body = MultipleReportsSerializer.serializer(reports)
        status = 200
        return body, status

    def post(self, data):
        report = self.create_new_report_interactor.set_params(data=data).execute()
        body = ReportSerializer.serializer(report)
        status = 200
        return body, status
