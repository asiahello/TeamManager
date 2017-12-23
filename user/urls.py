from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^(?P<pk>\d+)$', views.UserView.as_view(), name='userView'),
    url(r'^$', views.user_view, name='user-view'),
    # url(r'^coach/$', views.coach_view, name='coachView'),
    # url(r'^player/$', views.PlayerView.as_view(), name='playerView'),
]
