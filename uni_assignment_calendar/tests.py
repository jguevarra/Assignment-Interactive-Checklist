from django.test import TestCase
import unittest
from django.urls import reverse
from django.utils import timezone
from .models import Assignment
import datetime


# def create_event(event_text, days):
#     """
#     Create a question with the given `question_text` and published the
#     given number of `days` offset to now (negative for questions published
#     in the past, positive for questions that have yet to be published).
#     """
#     time = timezone.now() + datetime.timedelta(days=days)
#     return Event.objects.create(event_name=event_text, day=time)


# Testing Index View
class EventIndexViewTests(TestCase):
    def test_no_events(self):
        """
        If no post exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('calendar:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events have been posted.")

    # def test_future_events(self):
    #     """
    #     Post with a date in the future aren't displayed on
    #     the index page.
    #     """
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertContains(response, "No events have been posted.")
    #
    # def test_past_events(self):
    #     """
    #     Post with a date in the past aren't displayed on
    #     the index page.
    #     """
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertContains(response, "No events have been posted.")


# test for past posts, recent posts, future posts
# test for future and past posts in the case of the index page having multiple posts
