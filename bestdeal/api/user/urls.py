from django.urls import re_path
from . views import UserDetailView, CreateUserView, ManageUserView

urlpatterns = [
    re_path(r'^users/(?P<pk>[0-9a-f-]+)/$', UserDetailView.as_view(), name='user-detail'),
    re_path(r'^users/create/$', CreateUserView.as_view(), name='create'),
    re_path(r'^users/me/$', ManageUserView.as_view(), name='me'),
]
