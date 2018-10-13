import datetime

from django.db import models
from django.utils import timezone

# Post (title, description, post_date, due_date)
class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_details = models.CharField(max_length=500)
    post_date = models.DateTimeField('Date Posted')
    def __str__(self):
        return self.post_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    due_date = models.DateTimeField('Date of Event')

# list of classes for the user to choose from to post under
class Class(models.Model):
    classes = models.ForeignKey(Post, on_delete=models.CASCADE)
    classes_text = models.CharField(max_length=200)
    def __str__(self):
        return self.classes_text




# include post_class = models.CharField(max_length=200) -- to indicate/specify
# which class each post belongs to