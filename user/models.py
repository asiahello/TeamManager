from django.db import models
from django.contrib.auth.models import User

from team.models import Team, Club


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='player')
    position = models.CharField(max_length=20, verbose_name="pozycja")

    def __str__(self):
        return self.user.username


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coach')
    licence = models.CharField(max_length=20, verbose_name="Licencja")

    def __str__(self):
        return self.user.username
