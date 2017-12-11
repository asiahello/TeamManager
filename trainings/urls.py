from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^matches/$', views.matches_list, name='matches_list'),
    url(r'^(?P<event_id>\d+)/$', views.event_detail, name="event_detail"),
    url(r'^(?P<event_id>\d+)/share/$', views.training_share, name="training_share")
]
