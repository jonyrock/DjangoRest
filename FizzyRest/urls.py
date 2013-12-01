from django.conf.urls import patterns, url

urlpatterns = patterns('FizzyRestApp.views',
    url(r'^/?$', ''),
    url(r'^manufacturers/$', '_list'),
    url(r'^manufacturers/(?P<pk>[0-9]+)/$', 'snippet_detail'),
    url(r'^manufacturers/(?P<pk>[0-9]+)/drinks$', 'snippet_detail'),
)