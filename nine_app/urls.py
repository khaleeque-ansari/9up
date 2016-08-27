__author__ = 'khaleeque'

from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /tea-recipes/
    url(r'^$', views.index, name='index'),
    url(r'^first_time$', views.first_time, name='first_time'),
    url(r'^get_questions/$', views.get_questions, name='get_questions'),
    url(r'^get_questions/(?P<user_id>[0-9]+)/$', views.get_questions, name='get_questions'),
    url(r'^test$', views.test, name='test'),


]