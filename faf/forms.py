from django.forms import inlineformset_factory, ModelForm
from django.urls import reverse
from faf.models import SomaticsFactors, MotoricsFactors
from django.utils.translation import ugettext_lazy as _



class SomaticsFactorsForm(ModelForm):

    class Meta:
        model = SomaticsFactors
        exclude = ["bmi", "player"]
        help_texts = {
            'weight': _('w kg'),
            'height': _('w kg'),
        }


class MotoricsFactorsForm(ModelForm):

    class Meta:
        model = MotoricsFactors
        exclude = ["bmi", "player"]
