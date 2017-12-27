from user.models import Player, Team

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TeamForm


def user_is_coach_and_has_team(user, team_id):
    if user.is_authenticated:
        if hasattr(user, 'coach'):
            if user.coach.teams.filter(id=team_id).exists():
                return True


def team_detail(request, team_id):
    user = request.user
    team = get_object_or_404(Team, id=team_id)
    template = 'team/team_detail.html'

    if user_is_coach_and_has_team(user, team_id):
        return render(request, template, {'team': team, })
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")


def team_new(request):
    template = 'team/team_edit.html'
    user = request.user

    if user.is_authenticated:
        if hasattr(user, 'coach'):
            if request.method == "POST":
                form = TeamForm(request.POST)
                if form.is_valid():
                    new_team = form.save()
                    return redirect('team:team-detail', team_id=new_team.pk)
            else:
                form = TeamForm()
            return render(request, template, {'form': form, })


def team_delete(request, team_id):
    user = request.user
    team = get_object_or_404(Team, id=team_id)

    if user_is_coach_and_has_team(user, team_id):
        if request.method == 'POST':
            team.delete()
            return redirect('user:user-view')
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")
