from django.contrib import admin
from .models import Coach, Team, Club, Player

admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Club)