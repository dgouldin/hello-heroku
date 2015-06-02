import logging
import os
from django.conf.urls import url
from django.http import HttpResponse
logging.basicConfig(level=logging.DEBUG)

def hello_world(request):
    logging.info('saying hello')
    name = os.environ.get('NAME', 'World')
    return HttpResponse('Hello {}!'.format(name))

urlpatterns = [url(r'^$', hello_world)]
