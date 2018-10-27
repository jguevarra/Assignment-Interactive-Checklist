from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# from django.core.urlresolvers import reverse

# Create your models here.

# class Post(models.Model):
#     post_title = models.CharField(max_length=200)
#     post_description = models.CharField(max_length=1000)
#     post_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.post_title
#
#     # returns most recent published post
#     def was_published_recently(self):
#         return self.post_date >= timezone.now() - datetime.timedelta(days=1)

# class Class(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     class_text = models.CharField(max_length = 200)
#     def __str__(self):
#         return self.class_text

class Assignment(models.Model): # change all Events to Assignments
    assignment_name = models.CharField(max_length=200)
    due_date = models.DateTimeField(max_length=1000)
    pub_date = models.DateTimeField(u'date published')
    description = models.TextField(u'Description', help_text=u'Description', blank=True, null=True)
    def __str__(self):
        return self.assignment_name

    # returns most recent published post
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

#
# # the one that is being used right now
# class Event(models.Model):
#     event_name = models.TextField(u'Event Name', help_text=u'Event name', blank=True, null=True)
#     day = models.DateField(u'Day of the event', help_text=u'Day of the event')
#     start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
#     end_time = models.TimeField(u'Final time', help_text=u'Final time')
#     notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)
#     def __str__(self):
#         return self.event_name
#
#     class Meta:
#         verbose_name = u'Scheduling'
#         verbose_name_plural = u'Scheduling'
