from django.contrib import admin

from .models import Scheduler, Sprinkler

admin.site.register((Scheduler, Sprinkler))
