from django.contrib import admin

# Register your models here.

from .models import SomaticsFactors, MotoricsFactors

admin.site.register(SomaticsFactors)
admin.site.register(MotoricsFactors)
