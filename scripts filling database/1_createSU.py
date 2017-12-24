from django.contrib.auth.models import User

superuser = User.objects.create_user("jbaj", "jbaj@tm.com", "inzynierka")
superuser.is_superuser = True
superuser.is_staff = True
superuser.save()
