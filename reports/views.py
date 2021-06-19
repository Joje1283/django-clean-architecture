import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Report


@csrf_exempt
def reports(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        result = Report.objects.create(data=json.dumps(data))
        return JsonResponse(
            {'message': 'POST - hello django server', 'result': {'id': result.pk, 'data': json.loads(result.data)}})
