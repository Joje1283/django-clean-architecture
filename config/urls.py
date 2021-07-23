from django.urls import path, include
from django.contrib import admin

from reports.factories import create_reports_view
from .views import ViewWrapper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reports/', ViewWrapper.as_view(view_creator_func=create_reports_view), name='reports'),
]
