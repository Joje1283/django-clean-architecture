import json
from django.http import JsonResponse
from reports.models import Report


def monitors(request):
    if request.method == 'GET':
        series_data = list(
            map(lambda x: json.loads(x), list(Report.objects.order_by('-pk')[:10].values_list('data', flat=True))))
        return JsonResponse({'series': series_data})
