from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^home/$', home, name='home'),
    url(r'^workshop:(?P<workshop_key>[a-zA-Z0-9]+)/$', workshop, name='workshop'),
    url(r'^register/$', register, name='register'),
    url(r'^about/$', about, name='about'),
)
