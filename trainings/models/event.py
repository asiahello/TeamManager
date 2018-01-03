# -*- coding: utf-8 -*-

from datetime import timedelta
from django.db.models import Q
from user.models import Coach, Player

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class TrainingManager(models.Manager):
    def get_queryset(self):
        return super(TrainingManager, self).get_queryset().filter(type='training')


class MatchManager(models.Manager):
    def get_queryset(self):
        return super(MatchManager, self).get_queryset().filter(type='match')


class EventManager(models.Manager):

    def week_for_team(self, team_id, seven_days):
        # team = Team.objects.prefetch_related('trainings').get(id=team_id)
        return super(EventManager, self).get_queryset().filter(team__id=team_id).filter(date__range=[seven_days[0], seven_days[6]+timedelta(1)])

    def week_for_player(self, user_id, seven_days):
        # team = Team.objects.prefetch_related('trainings').get(id=team_id)
        return super(EventManager, self).get_queryset().filter(participants__user__id__contains=user_id).filter(date__range=[seven_days[0], seven_days[6]+timedelta(1)])

    def week_for_coach(self, user_id, seven_days):
        return super(EventManager, self).get_queryset().filter(performer__user__id=user_id).filter(date__range=[seven_days[0], seven_days[6]+timedelta(1)])


class Event(models.Model):
    EVENT_TYPE = (
        ('training', 'Trening'),
        ('match', 'Mecz'),
        ('meeting', 'Spotkanie'),
    )
    title = models.CharField(
        max_length=250,
        verbose_name="Tytuł",
        blank=True,
        default=""
    )
    date = models.DateTimeField(
        verbose_name="Data i godzina",
        default=timezone.now,
        blank=True
    )
    duration = models.IntegerField(
        verbose_name="Czas trwania",
        blank=True,
        default="90"
    )
    place = models.TextField(
        verbose_name="Miejsce",
        blank=True
    )
    type = models.CharField(
        max_length=10,
        verbose_name="Typ",
        choices=EVENT_TYPE,
        default='training',
    )
    author = models.ForeignKey(
        Coach,
        related_name='trainings_created',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="autor",
        blank=True,
        default=""
    )
    performer = models.ManyToManyField(
        Coach,
        related_name='trainings_performed',
        verbose_name="Wykonawca",
        # on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=""
    )
    content = models.TextField(
        verbose_name="Treść",
        blank=True,
        default=""
    )
    summary = models.TextField(
        verbose_name="Podsumowanie",
        blank=True,
        default=""
    )
    participants = models.ManyToManyField(
        Player,
        related_name="trainings",
        verbose_name="Uczestnicy",
        blank=True,
        default=""
    )
    team = models.ForeignKey(
        'team.Team',
        related_name="trainings",
        verbose_name="Zespół",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=""
    )

    # exercises = models.ManyToManyField(Exercise) #, related_name='intro_part_related_name')

    objects = EventManager()
    trainings = TrainingManager()  # returns only trainings
    matches = MatchManager()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trainings:training-detail', kwargs={'event_id': self.pk})
