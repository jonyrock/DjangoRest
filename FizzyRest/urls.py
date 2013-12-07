from django.conf.urls import patterns, url

urlpatterns = patterns('FizzyRestApp.views',
    url(r'^/?$', 'index'),
    url(r'^tasks/$', 'tasks_list'),
    url(r'^tasks/(?P<pk>[0-9]+)/?$', 'task_details')
)