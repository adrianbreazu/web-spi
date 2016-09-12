from django.contrib import admin

from .models import Scheduler, Sprinkler,Weather

admin.site.register((Scheduler, Sprinkler, Weather))
