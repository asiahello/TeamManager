from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^team/(?P<team_id>\d+)/new/$', views.training_new, name='training-new'),
    # url(r'^(?P<event_id>\d+)/$', views.training_detail, name="training-detail"),
    url(r'^team/(?P<team_id>\d+)/training/(?P<event_id>\d+)/delete/$', views.training_delete, name="training-delete"),


    url(r'^team/(?P<team_id>\d+)/$', views.get_this_week, name='training-team-list'),
    # /trainings/team/1/year/2017/week/50/
    url(r'^team/(?P<team_id>\d+)/year/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.training_team_week_list, name='training-team-week-list'),

    url(r'^matches/$', views.matches_list, name='matches_list'),
    url(r'^(?P<event_id>\d+)/share/$', views.training_share, name="training_share")
]
