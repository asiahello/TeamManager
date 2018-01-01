from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse_lazy

from team.models import Club, Team


class Player(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='player'
    )
    position = models.CharField(
        max_length=20,
        verbose_name="pozycja"
    )

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse_lazy('user:player-detail', kwargs={'player_id': self.pk})


class CoachClubManager(models.Manager):
    # def get_queryset(self):
    #     return super(CoachClubManager, self).get_queryset()

    def from_one_club(self, club_id):
        club = Club.objects.prefetch_related('teams').get(id=club_id)  # .filter(id=club_id).get()
        return super(CoachClubManager, self).get_queryset().filter(teams__in=club.teams.all())

    def train_player(self, player_id):
        player = Player.objects.prefetch_related('teams').get(id=player_id)  # .filter(id=player_id).get()
        return super(CoachClubManager, self).get_queryset().filter(teams__in=player.teams.all())


class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coach')
    licence = models.CharField(max_length=20, verbose_name="Licencja")

    objects = CoachClubManager()

    def __str__(self):
        return self.user.username



