from django.conf.urls import patterns, url

urlpatterns = patterns('polls.polls_views',
    url(r'^$', 'index'),
    url(r'(?P<poll_id>\d+)/$', 'detail'),
    url(r'(?P<poll_id>\d+)/results/$', 'results'),
    url(r'(?P<poll_id>\d+)/vote/$', 'vote'),
)
