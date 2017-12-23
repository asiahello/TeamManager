from django import forms
from django.db import models
from django.forms import ModelForm
from team.models import Club
from user.models import Player, Coach
#
# ACCOUNT_TYPE = (
#     ('Player', 'Zawodnik'),
#     ('Coach', 'Trener'),
# )
#
#
# class SignupForm(forms.Form):
#     first_name = forms.CharField(max_length=254, label='Imi?')
#     last_name = forms.CharField(max_length=254, label='Nazwisko')
#     account_type = forms.ChoiceField(choices=ACCOUNT_TYPE, label='Typ konta')
#     club = forms.ModelChoiceField(Club.objects.all(), label='Klub')
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.save()
#
#         if self.account_type == 'Player':
#             Player(
#                 user=user,
#                 club=self.club).save()
#             print("player")
#         elif self.account_type == 'Coach':
#             Coach(
#                 user=user,
#                 club=self.club).save()
#             print("coach")
