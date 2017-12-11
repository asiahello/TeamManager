from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .exercise import Exercise


class TrainingManager(models.Manager):
    def get_queryset(self):
        return super(TrainingManager, self).get_queryset().filter(type='training')


class MatchManager(models.Manager):
    def get_queryset(self):
        return super(MatchManager, self).get_queryset().filter(type='match')


class Event(models.Model):
    EVENT_TYPE = (
        ('training', 'Training'),
        ('match', 'Match'),
        ('meeting', 'Meeting'),
    )
    title = models.CharField(max_length=250, verbose_name="Tytuł", blank=True, default="")
    date = models.DateTimeField(default=timezone.now, verbose_name="Data i godzina", blank=True)
    duration = models.IntegerField(verbose_name="czas trwania", blank=True, default="90")
    place = models.TextField(verbose_name="miejsce", blank=True)
    type = models.CharField(max_length=10, choices=EVENT_TYPE, default='training', verbose_name="typ")
    author = models.ForeignKey(User, related_name='create_events', on_delete=models.SET_NULL, null=True, verbose_name="autor", blank=True, default="")
    performer = models.ForeignKey(User, related_name='perform_events', on_delete=models.SET_NULL, null=True, verbose_name="wykonujący", blank=True, default="")
    content = models.TextField(verbose_name="treść", blank=True, default="")
    summary = models.TextField(verbose_name="podsumowanie", blank=True, default="")
    participants = models.ManyToManyField(User, related_name="participate_events", blank=True, default="")

    exercises = models.ManyToManyField(Exercise) #, related_name='intro_part_related_name')

    objects = models.Manager()  # default manager
    trainings = TrainingManager()  # returns only trainings
    matches = MatchManager()

    class Meta:
        ordering = ('-date',)
        app_label = 'trainings'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('trainings:event_detail', kwargs={'event_id': self.pk})
