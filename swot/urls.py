from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new/$', views.swot_analysis_create, name='swot-new'),
#     url(r'^(?P<team_id>\d+)/delete/$', views.team_delete, name='team-delete'),
#     url(r'^new/$', views.team_new, name='team-new'),
]
