from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.user_view, name='user-view'),

    url(r'^player/new/$', views.player_new, name='player-new'),
    url(r'^player/(?P<player_id>\d+)$', views.player_detail, name='player-detail'),
    url(r'^player/(?P<player_id>\d+)/delete/$', views.player_delete, name='player-delete'),
    url(r'^player/swot/', include('swot.urls', namespace='swot', app_name='swot')),
    url(r'^player/faf/', include('faf.urls', namespace='faf', app_name='faf')),

    url(r'^player/update/(?P<player_id>\d+)$', views.PlayerUpdate.as_view(), name='player-update')

    # url(r'^coach/$', views.coach_view, name='coachView'),
    # url(r'^player/$', views.PlayerView.as_view(), name='playerView'),
]
