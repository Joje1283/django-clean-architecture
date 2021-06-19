import json

from django.http import JsonResponse
from django.db.models import F

from reports.models import Report


def monitors(request):
    if request.method == 'GET':
        series_data = list(Report.objects.order_by('-pk')[:10].annotate(sensors=F('data')).values('id', 'sensors'))
        return JsonResponse({'series': series_data})
