from django.conf.urls import patterns, url

from .views import index, register

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^pyworkshop/$', register, name='register'),
)
