from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from .viewsets import ScheduleViewSet
from rest_framework import routers

schedule_data_list = ScheduleViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
schedule_data_detail = ScheduleViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'', schedule_data_list, name='schedule-list'),
]
