from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, get_list_or_404, render

from user.models import Player, Coach


def user_view(request):
    user = request.user
    template = 'user/coach.html'

    if hasattr(user, 'coach'):
        print(user.username)
        teams = user.coach.teams.all()
        return render(request, template, {'user': user, 'role': 'coach', 'teams': teams})
    elif hasattr(user, 'player'):
        return render(request, template, {'user': user, 'role': 'player'})
