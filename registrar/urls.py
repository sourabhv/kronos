from django.conf.urls import patterns, url

from .views import index, thanks

urlpatterns = patterns('',
    url(r'^thanks', thanks, name='thanks'),
    url(r'^', index, name='index'),
)
