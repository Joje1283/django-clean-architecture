from django.urls import path
from .views import monitors

app_name = 'monitors'

urlpatterns = [
    path('', monitors)
]
