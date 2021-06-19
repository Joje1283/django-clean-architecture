import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms import model_to_dict

from .models import Report


@csrf_exempt
def reports(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        result = Report.objects.create(data=data)
        return JsonResponse({'message': 'POST - hello django server', 'data': model_to_dict(result)})
