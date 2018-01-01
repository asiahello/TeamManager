"""TeamManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
import team
urlpatterns = [

# nie wszystko musi byc w glownym, mozna pozagniezdzac jak swot

    url(r'^accounts/', include('allauth.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^admin/', admin.site.urls),
    url(r'^trainings/', include('trainings.urls', namespace='trainings', app_name='trainings')),
    url(r'^team/', include('team.urls', namespace='team', app_name='team')),

    url(r'^', include('user.urls', namespace='user', app_name='user')),
]

