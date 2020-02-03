from django.contrib import admin
from .models import team, hof, events

# Register your models here.
admin.site.register(team)
admin.site.register(hof)
admin.site.register(events)

