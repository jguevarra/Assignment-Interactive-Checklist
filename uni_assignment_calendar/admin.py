# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Assignment

admin.site.register(Assignment)

# registering the model
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'due_date', 'pub_date', 'description']
