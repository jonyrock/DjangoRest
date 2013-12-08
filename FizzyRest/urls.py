from django.conf.urls import patterns, url

urlpatterns = patterns('FizzyRestApp.views',
    url(r'^/?$', 'index'),
    url(r'^waiting/?$', 'waiting_list'),
    url(r'^done/?$', 'done_list'),
    url(r'^tasks/(?P<pk>[0-9]+)/?$', 'task_details')
)