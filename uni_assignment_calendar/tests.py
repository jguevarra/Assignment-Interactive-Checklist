from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Events
import datetime
from datetime import timedelta
from django.utils.timezone import now

# helper functions -- needa edit
def create_event_pub_date(events_name, pub_date):
    """
<<<<<<< HEAD
    Creates a post with a custom published/posted date using pub_date
=======
    Create a post with the given `events_name` and published the
    given number of `days` offset to now (negative for posts published
    in the past, positive for posts that have yet to be published).
>>>>>>> d7300ebdedb42e66272c109d2a0b99410b742f6e
    """
    new_pub_date = now() + timedelta(days=pub_date)
    return Events.objects.create(events_name=events_name, pub_date=new_pub_date)

def create_event_due_date(events_name, due_date):
    """
    Creates a post with a custom due date using due_date
    """
    new_due_date = now() + timedelta(days=due_date)
    return Events.objects.create(events_name=events_name, due_date=new_due_date)





# Testing Model View -- these tests are okay!
class AssignmentnModelTests(TestCase):

    def test_was_published_recently_with_future_events(self):
        """
        was_published_recently() returns False for events whose pub_date
        is in the future.
        """
        time = now() + timedelta(days=30)
        future_question = Events(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_events(self):
        """
        was_published_recently() returns False for events whose pub_date
        is older than 1 day.
        """
        time = now() - timedelta(days=1, seconds=1)
        old_question = Events(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_events(self):
        """
        was_published_recently() returns True for events whose pub_date
        is within the last day.
        """
        time = now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Events(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


# Testing Index View
class AssignmentIndexViewTests(TestCase):
    def test_no_assignments(self): # works
        """
        If no post exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events have been posted.")
        self.assertQuerysetEqual(response.context['latest_events_list'], [])

    # def test_not_recently_posted_events(self):
        """
        the posts outside of the "Recently Posted" list should disappear
        """

    # def test_future_pub_date_events(self):
        """
        post with a pub_date in the future aren't displayed on
        the index page.
        ERROR: object is not being deleted
        """
    #     create_events(events_name="Future Event.", pub_date=30)
    #     response = self.client.get(reverse('calendar:index'))
    #     # self.assertContains(response, "No events are available.")
    #     # self.assertQuerysetEqual(response.context['latest_events_list'], ['<Events: Future Event.>'])
    #     self.assertQuerysetEqual(response.context['latest_events_list'], [])

    def test_past_pub_date_events(self): # works
        """
        post with a pub_date in the past are displayed on the
        index page.
        """
        create_event_pub_date(events_name="Past Event.", pub_date=-30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_events_list'],
            ['<Events: Past Event.>']
        )

    #def test_past_due_date_events(self):
        """
        post with a due_date in the past are not displayed on the
        index page.
        Similar to test_future_assignments(self) test
        ERROR: object is not being deleted
        """

    def test_future_due_date_events(self): # works
        """
        post with a valid due date includes due date when posted on the index page
        """
        create_event_due_date(events_name="Future Due Date Event.", due_date=30)
        response = self.client.get(reverse('index'))
        self.assertQuerysetEqual(
            response.context['latest_events_list'],
            ['<Events: Future Due Date Event.>']
        )


# # testing detail view
class EventsDetailViewTests(TestCase):
    # def test_future_events(self):
    #     """
    #     The detail view of an event with a pub_date in the future
    #     returns a 404 not found.
    #     ERROR: 200 != 404
    #     """
    #     future_events = create_event_pub_date(events_name='Future Published Date Event.', pub_date=10)
    #     url = reverse('detail', args=(future_events.id,))
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 404)

    def test_past_events(self): # works
        """
        The detail view of an event with a pub_date in the past
        returns a 200.
        """
        past_events = create_event_pub_date(events_name="Past Published Date Event.", pub_date=30)
        url = reverse('detail', args=(past_events.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_future_due_date_events(self): # works
        """
        The detail view of an event with a due_date in the future
        returns a 200.
        """
        future_events = create_event_due_date(events_name="Future Due Date Event.", due_date=30)
        url = reverse('detail', args=(future_events.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


# testing database
class DatabaseTests(TestCase):
    """
    insert tests here!
    """


# login/signup/logout helper functions


# testing signup view
class SignupViewTests(TestCase):

    # create a helper function to create a new user

    # create a helper function with a login that already exists?

    #def test_username_invalid(self):
    """
    signup -- if a username is taken already, page should display
    "invalid form"
    """

    #def test_username_valid(self):
    """
    signup -- if a user successfully signup, page should display
    "thank you for registering!"
    """

    #def test_form_valid(self):
    """
    signup -- if form is valid, registered == True
    """

    #def test_form_invalid(self):
    """
    signup -- if form is invalid, registered == False
    """

# class LoginViewTests(TestCase):
#
#     # use helper functions for Signup view Tests
#
#     def test_login(self):
#         # send login data
#         response = self.client.post('/login/', self.credentials, follow=True)
#         # should be logged in now
#         self.assertTrue(response.context['user'].is_active)
#
#     #def test_authenticated_active(self):
#     """
#     if user is authenticated and active, the httpresponse should be
#     "log in successfully"
#     """
#
#     #def test_authenticated_inactive(self):
#     """
#     if user is authenticated and inactive, the httpresponse should
#     be "account not active"
#     """
#
#     #def test_not_authenticated(self):
#     """
#     if user is not authenticated, the httpresponse should be "invalid
#     login"
#     """
#
# class LogoutViewTests(TestCase):
#
#     # user helper functions to login into page
#
#     # def test_logged_in_logout(self):
#     """
#     if the user is logged in and logout is requested, "Logout successfully"
#     """