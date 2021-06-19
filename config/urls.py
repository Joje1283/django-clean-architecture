from django.contrib import admin
from django.urls import path
from django.http import JsonResponse


def test(request):
    if request.method == 'GET':
        data = request.GET.dict() if request.GET else {}
        return JsonResponse({'message': 'hello django server', 'data': data})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('update-sensor', test)
]
