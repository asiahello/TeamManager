from user.models import Coach, Player

from django.contrib.auth.models import User

Coach.objects.get_or_create(user=User.objects.filter(username="c1_t12_c1").get(), licence="UEFA")
Coach.objects.get_or_create(user=User.objects.filter(username="c2_t23_c1").get(), licence="UEFA")
Coach.objects.get_or_create(user=User.objects.filter(username="c3_t31_c1").get(), licence="UEFA")

Coach.objects.get_or_create(user=User.objects.filter(username="c1_t12_c2").get(), licence="UEFA")
Coach.objects.get_or_create(user=User.objects.filter(username="c2_t23_c2").get(), licence="UEFA")
Coach.objects.get_or_create(user=User.objects.filter(username="c3_t31_c2").get(), licence="UEFA")


Player.objects.create(user=User.objects.filter(username="p1_t1_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t1_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t1_c1").get(), position="0")

Player.objects.create(user=User.objects.filter(username="p1_t2_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t2_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t2_c1").get(), position="0")

Player.objects.create(user=User.objects.filter(username="p1_t3_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t3_c1").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t3_c1").get(), position="0")

Player.objects.create(user=User.objects.filter(username="p1_t1_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t1_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t1_c2").get(), position="0")

Player.objects.create(user=User.objects.filter(username="p1_t2_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t2_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t2_c2").get(), position="0")

Player.objects.create(user=User.objects.filter(username="p1_t3_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p2_t3_c2").get(), position="0")
Player.objects.create(user=User.objects.filter(username="p3_t3_c2").get(), position="0")
