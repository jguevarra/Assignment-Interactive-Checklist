from django.test import TestCase
import unittest
from django.urls import reverse
from django.utils import timezone
from .models import Assignment
import datetime


def create_assignment(assignment_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Assignment.objects.create(assignment_name=assignment_text, due_date=time)


# Testing Index View
class AssignmentIndexViewTests(TestCase):
    def test_no_assignments(self):
        """
        If no post exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('calendar:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No assignments have been posted.")


    # def test_future_assignemnts(self):
    #     """
    #     Post with a date in the future aren't displayed on
    #     the index page.
    #     """
    #     response = self.client.get(reverse('calendar:index'))
    #     self.assertContains(response, "No events have been posted.")
    #
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


# test for past posts, recent posts, future posts
# test for future and past posts in the case of the index page having multiple posts
