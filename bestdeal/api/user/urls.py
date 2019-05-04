from django.urls import re_path
from . views import UserDetailView

urlpatterns = [
    re_path(r'^users/(?P<pk>[0-9a-f-]+)/$', UserDetailView.as_view(), name='user-detail'),
]
