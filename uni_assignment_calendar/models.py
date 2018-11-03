from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Events(models.Model):
    class_abbrev = models.CharField(max_length=4)
    class_num = models.TextField(max_length=4, blank=True, null=True, default='')
    events_name = models.CharField(max_length=200)
    due_date = models.DateTimeField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.events_name

    # returns most recent published post
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    events = models.ForeignKey(Events, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


