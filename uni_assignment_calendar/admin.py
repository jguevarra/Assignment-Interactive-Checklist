# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Events

admin.site.register(Events)

# registering the model
class EventsAdmin(admin.ModelAdmin):
    list_display = ['class_abbrev', 'class_num', 'events_name', 'due_date', 'pub_date', 'description']
