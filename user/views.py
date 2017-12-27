from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PlayerForm
from .models import Coach, Player


def user_is_coach_and_has_player(user, player):
    if user.is_authenticated:
        if hasattr(user, 'coach'):
            if Coach.objects.train_player(player.id).exists():
                return True


def user_view(request):
    user = request.user
    template = 'user/coach/coach_detail.html'

    # TODO przebudowac
    if hasattr(user, 'coach'):
        teams = user.coach.teams.all()
        return render(request, template, {'user': user, 'role': 'coach', })
    elif hasattr(user, 'player'):
        return render(request, template, {'user': user, 'role': 'player', })


def player_detail(request, player_id):
    user = request.user
    player = get_object_or_404(Player, id=player_id)
    template = 'user/player/player_detail.html'

    if user_is_coach_and_has_player(user, player):
        return render(request, template, {'player': player, })
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")

    # TODO if user is player


def player_new(request):
    template = 'user/player/player_edit.html'
    user = request.user

    if user.is_authenticated and hasattr(user, 'coach'):
        if request.method == "POST":
            form = PlayerForm(request.POST)
            if form.is_valid():
                new_player = form.save()
                return redirect('training-team-list', team_id=new_player.pk)
        else:
            form = PlayerForm()
        return render(request, template, {'form': form, })


def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    user = request.user

    if user_is_coach_and_has_player(user, player):
        if request.method == 'POST':
            player.delete()
            return redirect('team:team-detail')
        else:
            return HttpResponse("<h1> Brak dost?pu </h1>")
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")



