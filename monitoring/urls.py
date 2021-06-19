from django.urls import path
from .views import reports

urlpatterns = [
    path('reports', reports),
]
