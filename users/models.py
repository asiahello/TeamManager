from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from trainings.models import AgeCategory


class Club(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    address = models.CharField(max_length=100, verbose_name="Adres", blank=True, default="")
    homepage = models.URLField()
    manager = models.ForeignKey(User, related_name='manager', on_delete=models.CASCADE, verbose_name="Manager")

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa")
    club = models.ForeignKey(Club, related_name='klub', on_delete=models.SET_NULL, verbose_name="Klub", null=True)
    age_category = models.ForeignKey(AgeCategory, related_name='kategoria_wiekowa', on_delete=models.SET_NULL, verbose_name="kategoria wiekowa", null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="+")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, verbose_name="dru?yna", null=True)
    position = models.CharField(max_length=20, verbose_name="pozycja")

    def __str__(self):
        return self.user.username


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="+")
    licence = models.CharField(max_length=20, verbose_name="Licencja")
    teams = models.ManyToManyField(Team, verbose_name="dru?yny", blank=True)

    def __str__(self):
        return self.user.username
