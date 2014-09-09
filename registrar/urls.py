from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^pyworkshop/$',register, name='register'),
    url(r'^pyworkshop/about/$', about, name='about'),
    url(r'^home/$',home, name='home'),
    url(r'^worshop:dropbox/$',dropbox, name='dropbox'),
    url(r'^workshop:pygame/$',pygame,name='pygame'),    
)
