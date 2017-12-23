from django.forms import ModelForm

from .models import Team
from user.models import Coach

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class CoachForm(ModelForm):
    class Meta:
        model = Coach
        fields = '__all__'
