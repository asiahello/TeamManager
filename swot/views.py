from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView
from swot.forms import SwotAnalyzisForm
from swot.models import Factor, PlayerFactor, SwotAnalysis


def assign_factors(swot):
    all_factors = Factor.objects.all()
    for factor in all_factors:
        swot.player_factors.add(PlayerFactor.objects.create(factor=factor, swot_analysis=swot))


def swot_analysis_create(request):
    user = request.user

    if user.is_authenticated() and hasattr(user, 'player'):
        player = user.player

        if not hasattr(player, 'swot'):
            swot = SwotAnalysis.objects.create(owner=player)
            assign_factors(swot)


        return redirect('user:player-detail', player_id=player.id)
    else:
        return HttpResponseRedirect("<h1> brak dostepu </h1>")