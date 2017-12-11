from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.MainRedirectView.as_view()),

    url(r'^login/$', RedirectView.as_view(url='/accounts/login/'), name="login"),

    url(r'^coach/$', views.CoachView.as_view(), name="coach-view"),
    url(r'^player/$', views.PlayerView.as_view(), name="player-view"),


    # url(r'^player/(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$', views.PlayerDashboardWeekArchiveView.as_view(),
    #     name="player-week"),
]