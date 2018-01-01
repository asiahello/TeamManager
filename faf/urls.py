from django.conf.urls import url

from . import views
from django.urls import reverse

urlpatterns = [
    url(r'^motorics/add/$', views.MotoricsCreate.as_view(), name='motorics-create'),
    url(r'^somatics/add/$', views.SomaticsCreate.as_view(), name='somatics-create'),

    url(r'^motorics/(?P<player_id>\d+)/$', views.MotoricsDetail.as_view(), name='motorics-detail'),


        #     url(r'^(?P<team_id>\d+)/delete/$', views.team_delete, name='team-delete'),
    #     url(r'^new/$', views.team_new, name='team-new'),
]
