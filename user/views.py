from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import UpdateView
from faf.charts import SomaticsChart
from faf.views import MotoricsDetail, get_motorics_tables_for_user

from .forms import PlayerForm
from .models import Coach, Player
from swot.models import ANALYSIS_CATEGORIES, SWOT_CATEGORIES, PlayerFactor


def user_is_coach_and_has_player(user, player):
    if user.is_authenticated:
        if hasattr(user, 'coach'):
            if Coach.objects.train_player(player.id).exists():
                return True


def user_view(request):
    if request.user.is_anonymous:
        return HttpResponseRedirect(reverse('account_login'))
    else:
        user = request.user
        if hasattr(user, 'coach'):
            template = 'user/coach/coach_detail.html'
            return render(request, template, {'user': user, 'role': 'coach', })
        elif hasattr(user, 'player'):
            return redirect('user:player-detail', player_id=user.player.id)
        else:
            return redirect('user:set-role')

def set_role(request):
    template = 'user/set_role.html'
    return render(request, template, {'user': request.user})


def player_detail(request, player_id):
    user = request.user
    player = get_object_or_404(Player, id=player_id)
    template = 'user/player/player_detail.html'

    strength_table, endurance_table, velocity_table, coordination_table = get_motorics_tables_for_user(request, player_id)
    player_factors = PlayerFactor.objects.filter(swot_analysis__owner__id=player_id)

    context = {
        'player': player,

        'somatics_chart': SomaticsChart(),
        'motorics_factors_tables': MotoricsDetail,
        'strength_table': strength_table,
        'endurance_table': endurance_table,
        'velocity_table': velocity_table,
        'coordination_table': coordination_table,

        'analysis_categories': ANALYSIS_CATEGORIES,
        # 'swot_categories': SWOT_CATEGORIES,
        'player_factors': player_factors
    }
    if user_is_coach_and_has_player(user, player):
        # rather return view for coach
        return render(request, template, {'player': player, })
    elif user.player.id == player.id:
        return render(request, template, context)
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")


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


# TODO to mo?e by? to przypisanie usera do zawodnika - tylko dla trenera
class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'user/player/player_update.html'

    def get_object(self):
        return Player.objects.get(pk=self.request.user.player.id)
