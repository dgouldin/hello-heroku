from django.conf.urls import url
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('Hello World!')

urlpatterns = [url(r'^$', hello_world)]
