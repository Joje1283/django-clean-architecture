import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def reports(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'POST - hello django server', 'data': data})
