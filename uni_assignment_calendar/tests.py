from django.test import TestCase
import unittest
from django.urls import reverse
from django.utils import timezone
from .models import Events
import datetime


def create_events(events_name, pub_date):
    """
    Create a post with the given `events_name` and published the
    given number of `days` offset to now (negative for psots published
    in the past, positive for psots that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=pub_date)
    return Events.objects.create(events_name=events_name, pub_date=time)


# Testing Model View
class AssignmentnModelTests(TestCase):

    def test_was_published_recently_with_future_events(self):
        """
        was_published_recently() returns False for events whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Events(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_events(self):
        """
        was_published_recently() returns False for events whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Events(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_events(self):
        """
        was_published_recently() returns True for events whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Events(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# Testing Index View
class AssignmentIndexViewTests(TestCase):
    def test_no_assignments(self):
        """
        If no post exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('calendar:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events have been posted.")
        self.assertQuerysetEqual(response.context['latest_events_list'], [])

    def test_future_assignments(self):

        """
        post with a pub_date in the future aren't displayed on
        the index page.
        """
        create_events(events_name="Future Event.", pub_date=30)
        response = self.client.get(reverse('calendar:index'))
        self.assertContains(response, "No events are available.")
        self.assertQuerysetEqual(response.context['latest_events_list'], [])

    # def test_past_events(self):
    #     """
    #     post with a pub_date in the past are displayed on the
    #     index page.
    #     """
    #     create_events(events_name="Past Event", due_date=-30)
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         ['<Question: Past question.>']
    #     )

        """
        post with a due_date in the past are not displayed on the
        index page.
        Similar to the test where no posts exist
        """


        """
        post with a valid due date includes due date when posted on the index page
        """

# testing detail view
# class EventsDetailViewTests(TestCase):
#     def test_future_events(self):
        """
        The detail view of an event with a pub_date in the future
        returns a 404 not found.
        """
#         future_events = create_events(events_name='Future Events.', due_date=5)
#         url = reverse('calendar:detail', args=(future_events.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

        """
        The detail view of an event with a due_date in the past
        returns a 404 not found.
        """


# test for past posts, recent posts, future posts
# test for future and past posts in the case of the index page having multiple posts
