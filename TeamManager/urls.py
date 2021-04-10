# from django.conf.urls import include, url
# from django.contrib import admin
# import team

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

# nie wszystko musi byc w glownym, mozna pozagniezdzac jak swot

    path(r'accounts/', include('allauth.urls')),
    path(r'messages/', include('postman.urls', namespace='postman')),
    path(r'admin/', admin.site.urls),
    path(r'trainings/', include('trainings.urls', namespace='trainings')),
    path(r'team/', include('team.urls', namespace='team')),
    path(r'swot/', include('swot.urls', namespace='swot')),
    path(r'', include('user.urls', namespace='user'))
]

