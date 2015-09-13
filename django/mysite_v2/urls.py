from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import admin
admin.autodiscover()

handler404 = 'mysite.mysite_views.error_404'
handler500 = 'mysite.mysite_views.error_500'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mysite/', include('mysite.mysite_urls')),
    url(r'^polls/', include('polls.polls_urls')),
)
