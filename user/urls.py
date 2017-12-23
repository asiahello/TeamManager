from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<pk>\d+)$', views.UserView.as_view(), name='userView'),
    url(r'^$', views.user_view, name='user-view'),

    url(r'^player/new/$', views.player_new, name='player-new'),
    url(r'^player/(?P<player_id>\d+)$', views.player_detail, name='player-detail'),
    url(r'^player/(?P<player_id>\d+)/delete/$', views.player_delete, name='player-delete'),

    # url(r'^coach/$', views.coach_view, name='coachView'),
    # url(r'^player/$', views.PlayerView.as_view(), name='playerView'),
]


