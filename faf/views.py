from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django_tables2 import RequestConfig
from faf.forms import MotoricsFactorsForm, SomaticsFactorsForm
from faf.models import MotoricsFactors, SomaticsFactors
from faf.tables import MotoricsStrenghtTable, MotoricsEnduranceTable, MotoricsCoordinationTable, MotoricsVelocityTable

class MotoricsCreate(CreateView):
    form_class = MotoricsFactorsForm
    template_name = 'faf/motorics_create.html'

    def form_valid(self, form):
        s = form.save(commit=False)
        s.player = self.request.user.player
        s.save()
        return super(MotoricsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user:player-detail',  kwargs={'player_id': self.request.user.player.id})



def get_motorics_tables_for_user(request, player_id):

    mf = MotoricsFactors.objects.user_params(player_id)
    strength_table = MotoricsStrenghtTable(mf)
    endurance_table = MotoricsEnduranceTable(mf)
    velocity_table = MotoricsVelocityTable(mf)
    coordination_table = MotoricsCoordinationTable(mf)

    RequestConfig(request).configure(strength_table)
    RequestConfig(request).configure(endurance_table)
    RequestConfig(request).configure(velocity_table)
    RequestConfig(request).configure(coordination_table)

    return strength_table, endurance_table, velocity_table, coordination_table

class MotoricsDetail(DetailView):
    model = MotoricsFactors
    template_name = "faf/motorics_detail.html"

    def get_context_data(self, **kwargs):
        context = super(MotoricsDetail, self).get_context_data(**kwargs)
        mf = MotoricsFactors.objects.user_params(self.kwargs['player_id'])
        context['test'] = 1

        # strength_table = MotoricsStrenghtTable(mf)
        # endurance_table = MotoricsEnduranceTable(mf)
        # velocity_table = MotoricsVelocityTable(mf)
        # coordination_table = MotoricsCoordinationTable(mf)
        #
        # RequestConfig(self.request).configure(strength_table)
        # RequestConfig(self.request).configure(endurance_table)
        # RequestConfig(self.request).configure(velocity_table)
        # RequestConfig(self.request).configure(coordination_table)
        #
        # context['strength_table'] = strength_table
        # context['endurance_table'] = endurance_table
        # context['velocity_table'] = velocity_table
        # context['coordination_table'] = coordination_table

        # print(strength_table)

        return context


class SomaticsCreate(CreateView):
    form_class = SomaticsFactorsForm
    template_name = 'faf/somatics_create.html'

    def form_valid(self, form):
        s = form.save(commit=False)
        s.bmi = s.weight / (s.height/100 * s.height/100)
        s.player = self.request.user.player
        s.save()
        return super(SomaticsCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user:player-detail',  kwargs={'player_id': self.request.user.player.id})
