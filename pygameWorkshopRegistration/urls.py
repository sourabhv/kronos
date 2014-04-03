from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'pygameWorkshopRegistration.views.home', name='home'),
    # url(r'^pygameWorkshopRegistration/', include('pygameWorkshopRegistration.foo.urls')),

)
