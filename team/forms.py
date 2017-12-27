from user.models import Coach

from django.forms import ModelForm

from .models import Team


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'
