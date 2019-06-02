from django.urls import re_path
from . views import BrandListView, BrandDetailView

urlpatterns = [
    # sans les deals
    re_path(r'^brands/$', BrandListView.as_view(), name='brand-list-nofk'),
    re_path(r'^brands/(?P<pk>[0-9a-f-]+)/$',
            BrandDetailView.as_view(), name='brand-detail'),
]
