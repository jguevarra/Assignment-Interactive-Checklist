from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_description = models.CharField(max_length=1000)
    post_date = models.DateTimeField('date published')
    def __str__(self):
        return self.post_title

    # returns most recent published post
    def was_published_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)

class Class(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    class_text = models.CharField(max_length = 200)
    def __str__(self):
        return self.class_text


# for creating the calendar
class Event(models.Model):
    event_name = models.TextField(u'Event Name', help_text=u'Event name', blank=True, null=True)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    # validations
    # checks if there are overlapping events; are there collisions?
    # def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
    #     overlap = False
    #     if new_start == fixed_end or new_end == fixed_start:  # edge case
    #         overlap = False
    #     elif (new_start >= fixed_start and new_start <= fixed_end) or (
    #             new_end >= fixed_start and new_end <= fixed_end):  # innner limits
    #         overlap = True
    #     elif new_start <= fixed_start and new_end >= fixed_end:  # outter limits
    #         overlap = True
    #
    #     return overlap
    #
    # def get_absolute_url(self):
    #     url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
    #     return u'<a href="%s">%s</a>' % (url, str(self.start_time))
    #
    # def clean(self):
    #     if self.end_time <= self.start_time:
    #         raise ValidationError('Ending times must after starting times')
    #
    #     events = Event.objects.filter(day=self.day)
    #     if events.exists():
    #         for event in events:
    #             if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
    #                 raise ValidationError(
    #                     'There is an overlap with another event: ' + str(event.day) + ', ' + str(
    #                         event.start_time) + '-' + str(event.end_time))