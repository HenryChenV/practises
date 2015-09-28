from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page

from mysite_views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mysite',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^context_processor/$', 'mysite_views.mytime'),
    url(r'^database_caching/$', 'mysite_views.test_database_caching'),
    url(r'^cache_page/$', cache_page(60)(test_cache_page)),
    url(r'^dont_cache_page/$', test_cache_page),
)
