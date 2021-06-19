from django.urls import path
from .views import reports

app_name = 'reports'

urlpatterns = [
    path('', reports),
]
