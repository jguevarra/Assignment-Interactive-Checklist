from django.test import TestCase
import unittest
from django.urls import reverse
from django.utils import timezone
from .models import Events
import datetime


def create_events(events_text, due_date):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(due_date=due_date)
    return Events.objects.create(events_name=events_text, due_date=time)


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
        self.assertContains(response, "No assignments have been posted.")
    #
    # def test_future_assignemnts(self):
    #     """
    #     assignment with a date in the future aren't displayed on
    #     the index page.
    #     """
    #     create_assignment(question_text="Future assignment.", days=30)
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertContains(response, "No assignments are available.")
    #     self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # def test_past_events(self):
    #     """
    #     Questions with a pub_date in the past are displayed on the
    #     index page.
    #     """
    #     create_assignment(assignment_text="Past assignment", days=-30)
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_question_list'],
    #         ['<Question: Past question.>']
    #     )

# testing detail view
# class QuestionDetailViewTests(TestCase):
#     def test_future_assignment(self):
#         """
#         The detail view of a question with a pub_date in the future
#         returns a 404 not found.
#         """
#         future_assignment = create_assignment(assignment_text='Future assignment.', days=5)
#         url = reverse('calendar:detail', args=(future_assignment.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 404)

# test for past posts, recent posts, future posts
# test for future and past posts in the case of the index page having multiple posts
