
from django.contrib import admin
from django.urls import path

from CCD.views import MonitoringAddView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/add/', MonitoringAddView.as_view(), name="add_news")
]
