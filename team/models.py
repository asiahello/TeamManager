from django.contrib.auth.models import User
from django.db import models


class Club(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nazwa"
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Adres",
        blank=True,
        default=""
    )
    homepage = models.URLField(
    )
    manager = models.ForeignKey(
        User,
        related_name='manager',
        on_delete=models.CASCADE,
        verbose_name="Manager"
    )

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Nazwa"
    )
    club = models.ForeignKey(
        Club,
        related_name='teams',
        on_delete=models.SET_NULL,
        verbose_name="Klub",
        null=True
    )
    players = models.ManyToManyField(
        'user.Player',
        verbose_name="Zawodnicy",
        related_name='teams'
    )

    # age_category = models.ForeignKey(AgeCategory, related_name='kategoria_wiekowa', on_delete=models.SET_NULL, verbose_name="kategoria wiekowa", null=True)

    coaches = models.ManyToManyField(
        'user.Coach',
        verbose_name="trenerzy",
        blank=True,
        related_name='teams'
    )

    def __str__(self):
        return self.name
