from django.urls import re_path
from bestdeal.api.deal.views import DealListView, DealDetailView, DealNoFk


urlpatterns = [
    re_path(r'^deals/$', DealListView.as_view(), name='deal-list'),
    re_path(r'^deals/(?P<pk>[0-9a-f-]+)/$', DealDetailView.as_view(), name='deal-detail'),
    re_path(r'^deals/nofk/$', DealNoFk.as_view(), name='deal-list-all'),
]
