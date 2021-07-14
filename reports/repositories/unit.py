
class ReportRepo:
    def __init__(self, db_repo, cache_repo=None):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def get_recently_reports(self):
        return self.db_repo.get_recently_reports()

    def create_report(self, report):
        return self.db_repo.create_report(report)
