from django.conf import settings
from django.conf.urls import patterns, include, url
# serve the static files
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('registrar.urls', namespace='registrar')),
)

# the following function will only work if DEBUG is True and STATIC_URL
# setting is not empty
# TODO: check if the following code works for heroku.

#urlpatterns += staticfiles_urlpatterns

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
