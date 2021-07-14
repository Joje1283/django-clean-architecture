class MultipleReportsSerializer:
    @staticmethod
    def serializer(reports):
        return [ReportSerializer.serializer(report) for report in reports]


class ReportSerializer:
    @staticmethod
    def serializer(report):
        return {
            'id': str(report.id),
            'data': report.data
        }
