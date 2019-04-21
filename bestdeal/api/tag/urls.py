from django.urls import re_path
from . views import TagListView, TagDetailView, TagFk


urlpatterns = [
    # sans deal
    re_path(r'^tags/$', TagListView.as_view(), name='tag-list-nofk'),
    re_path(r'^tags/(?P<pk>[0-9a-f-]+)/$', TagDetailView.as_view(), name='tag-detail'),
    # avec deal
    re_path(r'^tags/fk/$', TagFk.as_view(), name='tag-list-fk'),
]
