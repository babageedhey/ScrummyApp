from django.contrib import admin
from .models import ScrumGoal
from .models import ScrumUser
from . import models



#Register your models here.
admin.site.register(models.ScrumUser)
admin.site.register(models.ScrumGoal)

