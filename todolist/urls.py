from django.conf.urls import patterns, include, url
from django.contrib import admin
from todo.views import TaskView, login_view, logout_view, change_task_status

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^todo/login/$', login_view),
    url(r'^todo/logout/$', logout_view),
    url(r'^todo/list/$', TaskView.as_view()),
    url(r'^todo/change_status/$', change_task_status),
)
