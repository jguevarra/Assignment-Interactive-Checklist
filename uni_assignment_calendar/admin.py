# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Events, Courses, Enrollment

admin.site.register(Events)
admin.site.register(Courses)
admin.site.register(Enrollment)
