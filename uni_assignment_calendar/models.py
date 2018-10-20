import datetime

from django.db import models
from django.utils import timezone

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
