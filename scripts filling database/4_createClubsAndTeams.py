from user.models import Coach, Player

from django.contrib.auth.models import User

from team.models import Club, Team

_manager = User.objects.filter(username='jbaj').get()

club1, created = Club.objects.get_or_create(name="club1", homepage="club1.pl", manager=_manager)
club2, created = Club.objects.get_or_create(name="club2", homepage="club2.pl", manager=_manager)


# CLUB 1

t1_c1, created = Team.objects.get_or_create(name="t1_c1", club=club1)

if created:
    t1_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c1_t12_c1").get()).get())
    t1_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c3_t31_c1").get()).get())
    t1_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t1_c1").get()).get())
    t1_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t1_c1").get()).get())
    t1_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t1_c1").get()).get())
    t1_c1.save()


t2_c1, created = Team.objects.get_or_create(name="t2_c1", club=club1)

if created:
    t2_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c1_t12_c1").get()).get())
    t2_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c2_t23_c1").get()).get())
    t2_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t2_c1").get()).get())
    t2_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t2_c1").get()).get())
    t2_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t2_c1").get()).get())
    t2_c1.save()


t3_c1, created = Team.objects.get_or_create(name="t3_c1", club=club1)

if created:
    t3_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c2_t23_c1").get()).get())
    t3_c1.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c3_t31_c1").get()).get())
    t3_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t3_c1").get()).get())
    t3_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t3_c1").get()).get())
    t3_c1.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t3_c1").get()).get())
    t3_c1.save()


# CLUB2

t1_c2, created = Team.objects.get_or_create(name="t1_c2", club=club2)

if created:
    t1_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c1_t12_c2").get()).get())
    t1_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c3_t31_c2").get()).get())
    t1_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t1_c2").get()).get())
    t1_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t1_c2").get()).get())
    t1_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t1_c2").get()).get())
    t1_c2.save()


t2_c2, created = Team.objects.get_or_create(name="t2_c2", club=club2)

if created:
    t2_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c1_t12_c2").get()).get())
    t2_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c2_t23_c2").get()).get())
    t2_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t2_c2").get()).get())
    t2_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t2_c2").get()).get())
    t2_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t2_c2").get()).get())
    t2_c2.save()


t3_c2, created = Team.objects.get_or_create(name="t3_c2", club=club2)

if created:
    t3_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c2_t23_c2").get()).get())
    t3_c2.coaches.add(Coach.objects.filter(user=User.objects.filter(username="c3_t31_c2").get()).get())
    t3_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p1_t3_c2").get()).get())
    t3_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p2_t3_c2").get()).get())
    t3_c2.players.add(Player.objects.filter(user=User.objects.filter(username="p3_t3_c2").get()).get())
    t3_c2.save()
