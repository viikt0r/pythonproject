from django.urls import re_path
from . views import AbuseListView, AbuseDetailView


urlpatterns = [
    re_path(r'^abuse-report/$', AbuseListView.as_view(), name='abuse-list'),
    re_path(r'^abuse-report/(?P<pk>[0-9a-f-]+)/$', AbuseDetailView.as_view(), name='abuse-detail'),
]