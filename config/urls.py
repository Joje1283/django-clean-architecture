from django.urls import path, include
from django.contrib import admin

"""
url architecture

domain/monitors/  device id
domain/reports/  
domain/rooms/
domain/devices/
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports', include('reports.urls')),
    path('monitors', include('monitors.urls')),
]
