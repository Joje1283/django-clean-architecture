import json

from django.test import TestCase
from reports.models import Report
from django.urls import reverse


class ReportApiTest(TestCase):
    def setUp(self) -> None:
        Report.objects.create(data={"name": "jaesik", "age": 21})

    def test_get_report(self):
        response = self.client.get(reverse('reports'))
        self.assertEqual(response.status_code, 200)

    def test_post_reports(self):
        report_data = {"name": "jaesik", "age": 21}
        response = self.client.post(path=reverse('reports'), data={'data': report_data},
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(report_data, json.loads(response.content).get('data'))
