from __future__ import unicode_literals

import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.postgres.fields import ArrayField 

class Courses(models.Model):
    class_id = models.IntegerField(primary_key=True, null=False, default=0)
    class_abbrev = models.CharField(max_length=4)
    class_num = models.TextField(max_length=4, blank=True, null=True, default='')
    class_title = models.TextField(max_length=50)
    instructor = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    class Meta:
        ordering = ["class_title"]
    def __str__(self):
        return self.class_title


class Events(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, default=0)
    events_name = models.CharField(max_length=200)
    due_date = models.DateField(null=True)
    due_time = models.TimeField((u"Due Time"), blank=True, default="11:59")
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    users = ArrayField(models.CharField(max_length=50))
    checked_users = ArrayField(models.CharField(max_length=50))
    def __str__(self):
        return self.events_name

    # returns most recent published post
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

# class Choice(models.Model):
#     events = models.ForeignKey(Events, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#     def __str__(self):
#         return self.choice_text


class Enrollment(models.Model):
    username = models.CharField(max_length=200)
    class_id = models.IntegerField(max_length=10)
    def __str__(self):
        return self.username + " enrolled in " + str(self.class_id)
'''
class Blacklist(models.Model):
    username = models.CharField(max_length=200)
    block = models.IntegerField(max_length=10)
    def __str__(self):
        return self.block
'''