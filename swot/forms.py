from django.forms import ModelForm
from swot.models import SwotAnalysis


class SwotAnalyzisForm(ModelForm):

    class Meta:
        model = SwotAnalysis
        exclude = '__all__'
