from django.forms import ModelForm, ModelMultipleChoiceField
from django.forms.models import inlineformset_factory

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

# CoachFormSet = inlineformset_factory(Team, Coach, form=CoachForm, extra=1)