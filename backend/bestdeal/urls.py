from os import listdir
from os.path import join, isdir
from django.urls import path, include
from pythonproject.settings import BASE_DIR
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Bestdeal API')

API_DIR = 'bestdeal/api/'
entities = [directory
            for directory in listdir(join(BASE_DIR, API_DIR))
            if (isdir(join(BASE_DIR, API_DIR, directory))
                and directory != '__pycache__')]

urlpatterns = [
    path('', include('bestdeal.api.{}.urls'.format(entity)))
    for entity in entities
]


urlpatterns += [
    path('docs/', schema_view),
]