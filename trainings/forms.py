from django import forms
from django.forms import Textarea
from trainings.models import Comment, Event


class EmailEventForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class TrainingForm(forms.ModelForm):

    class Meta:
            model = Event
            exclude = ['author', 'participants']
            fields = '__all__'
            # widgets = {
            #     # 'title': Textarea(attrs={'cols': 80, 'rows': 20}),
            # }

    def __init__(self, teams, *args, **kwargs):
        self.fields['team'].queryset = teams
        super(TrainingForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')



