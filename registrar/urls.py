from django.conf.urls import patterns, url
from django.conf import settings

from .views import index

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.contrib.staticfiles.views', {'document_root': settings.STATIC_ROOT}),
    )
