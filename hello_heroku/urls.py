import logging
from django.conf.urls import url
from django.http import HttpResponse
logging.basicConfig(level=logging.DEBUG)

def hello_world(request):
    logging.info('saying hello')
    return HttpResponse('Hello World!')

urlpatterns = [url(r'^$', hello_world)]
