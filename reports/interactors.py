from .entities import Report


class GetRecentlyReportsInteractor:
    def __init__(self, report_repo):
        self.report_repo = report_repo

    def set_params(self):
        return self

    def execute(self):
        return self.report_repo.get_recently_reports()


class CreateReportInteractor:
    def __init__(self, report_repo):
        self.report_repo = report_repo

    def set_params(self, data):
        self.data = data
        return self

    def execute(self):
        report = Report(data=self.data)
        # permission check
        # validation check
        return self.report_repo.create_report(report)
