from django.contrib.auth.models import User
from team.models import Club, Team
from user.models import Player, Coach

_manager = User.objects.filter(username='jbaj').get()

club1, created = Club.objects.get_or_create(name="club1", homepage="club1.pl", manager=_manager)
club2, created = Club.objects.get_or_create(name="club2", homepage="club2.pl", manager=_manager)

coach110, created = Coach.objects.get_or_create(user=User.objects.filter(username="110").get(), licence="UEFA")
coach120, created = Coach.objects.get_or_create(user=User.objects.filter(username="120").get(), licence="UEFA")
coach130, created = Coach.objects.get_or_create(user=User.objects.filter(username="130").get(), licence="UEFA")

coach210, created = Coach.objects.get_or_create(user=User.objects.filter(username="210").get(), licence="UEFA")
coach220, created = Coach.objects.get_or_create(user=User.objects.filter(username="220").get(), licence="UEFA")
coach230, created = Coach.objects.get_or_create(user=User.objects.filter(username="230").get(), licence="UEFA")

team11, created = Team.objects.get_or_create(name="team11", club=club1)
if created:
    team11.coaches.add(coach110, coach120)
    team11.save()

team12, created = Team.objects.get_or_create(name="team12", club=club1)
if created:
    team12.coaches.add(coach120, coach130)
    team12.save()

team13, created = Team.objects.get_or_create(name="team13", club=club1)
if created:
    team13.coaches.add(coach130, coach110)
    team13.save()


team21, created = Team.objects.get_or_create(name="team21", club=club2)
if created:
    team21.coaches.add(coach210, coach220)
    team21.save()

team22, created = Team.objects.get_or_create(name="team22", club=club2)
if created:
    team22.coaches.add(coach220, coach230)
    team22.save()

team23, created = Team.objects.get_or_create(name="team23", club=club2)
if created:
    team23.coaches.add(coach230, coach210)
    team23.save()


Player.objects.create(user=User.objects.filter(username="111").get(), team=team11, position="0")
Player.objects.create(user=User.objects.filter(username="112").get(), team=team11, position="0")
Player.objects.create(user=User.objects.filter(username="113").get(), team=team11, position="0")

Player.objects.create(user=User.objects.filter(username="121").get(), team=team12, position="0")
Player.objects.create(user=User.objects.filter(username="132").get(), team=team12, position="0")
Player.objects.create(user=User.objects.filter(username="123").get(), team=team12, position="0")

Player.objects.create(user=User.objects.filter(username="131").get(), team=team13, position="0")
Player.objects.create(user=User.objects.filter(username="132").get(), team=team13, position="0")
Player.objects.create(user=User.objects.filter(username="133").get(), team=team13, position="0")

Player.objects.create(user=User.objects.filter(username="211").get(), team=team21, position="0")
Player.objects.create(user=User.objects.filter(username="212").get(), team=team21, position="0")
Player.objects.create(user=User.objects.filter(username="213").get(), team=team21, position="0")

Player.objects.create(user=User.objects.filter(username="221").get(), team=team22, position="0")
Player.objects.create(user=User.objects.filter(username="222").get(), team=team22, position="0")
Player.objects.create(user=User.objects.filter(username="223").get(), team=team22, position="0")

Player.objects.create(user=User.objects.filter(username="231").get(), team=team23, position="0")
Player.objects.create(user=User.objects.filter(username="232").get(), team=team23, position="0")
Player.objects.create(user=User.objects.filter(username="233").get(), team=team23, position="0")
