from django.db import models

# Create your models here.
from django.utils import timezone
from user.models import Player


class SomaticsManager(models.Manager):

    def user_params(self, player_id):
        return super(SomaticsManager, self).get_queryset().filter(player__id=player_id)


class MotoricsManager(models.Manager):

    def user_params(self, player_id):
        return super(MotoricsManager, self).get_queryset().filter(player__id=player_id)


class SomaticsFactors(models.Model):
    date = models.DateField(
        verbose_name="Data",
        default=timezone.now,
        blank=True
    )
    height = models.FloatField()
    weight = models.FloatField()
    bmi = models.FloatField() # masa / wzrost^2
    fat = models.FloatField()
    player = models.ForeignKey(
        Player,
        related_name='somatics_factors',
        on_delete=models.CASCADE,
        verbose_name="owner",
        blank=True,
        null=True,
        default=""
    )

    objects = SomaticsManager()


class MotoricsFactors(models.Model):
    date = models.DateField(
        verbose_name="Data",
        default=timezone.now,
        blank=True
    )
    strength = models.CharField(
        max_length=300,
        verbose_name="Si?a",
    )
    endurance = models.CharField(
        max_length=300,
        verbose_name="Wytrzyma?o??",
    )
    velocity = models.CharField(
        max_length=300,
        verbose_name="Szybko??",

    )
    coordination = models.CharField(
        max_length=300,
        verbose_name="Koordynacja",
    )
    player = models.ForeignKey(
        Player,
        related_name='motorics_factors',
        on_delete=models.CASCADE,
        verbose_name="owner",
        blank=True,
        null=True,
        default=""
    )

    objects = MotoricsManager()


