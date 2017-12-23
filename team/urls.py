from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<team_id>\d+)$', views.team_detail, name='team-detail'),
    url(r'^(?P<team_id>\d+)/delete/$', views.team_delete, name='team-delete'),
    url(r'^new/$', views.team_new, name='team-new'),
    #url(r'^$', views.user_view, name='userView'),
    # url(r'^coach/$', views.coach_view, name='coachView'),
    # url(r'^$', views.PlayerListView.as_view(), name='players'),
]
