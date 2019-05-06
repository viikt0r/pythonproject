from django.urls import re_path
from . views import TagListView, TagDetailView


urlpatterns = [
    # sans deal
    re_path(r'^tags/$', TagListView.as_view(), name='tag-list-nofk'),
    re_path(r'^tags/(?P<pk>[0-9a-f-]+)/$', TagDetailView.as_view(), name='tag-detail'),
]
