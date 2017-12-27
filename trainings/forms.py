from django import forms

from trainings.models import Comment, Event


class EmailEventForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class TrainingForm(forms.ModelForm):

    x = {}

    def __init__(self, *args, **kwargs):
        super(TrainingForm, self).__init__(*args, **kwargs)
        initial = kwargs.get('initial')
        if initial is not None:
            self.fields['performer'].queryset = initial.get('performer')

    class Meta:
                model = Event
                exclude = ['author', 'participants', 'team']
                fields = '__all__'
                # widgets = {
                #     # 'title': Textarea(attrs={'cols': 80, 'rows': 20}),
                # }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
