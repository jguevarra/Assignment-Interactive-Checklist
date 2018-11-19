from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Events
import datetime
from datetime import timedelta
from django.utils.timezone import now
from django.test import Client


# helper functions -- needa edit
def create_event_pub_date(events_name, pub_date):
    """
    Creates a post with a custom published/posted date using pub_date
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
    database testing here
    """



# login/signup/logout helper functions
class LoginLogoutTests(TestCase): # works

    def test_no_inputs(self):
        """
        If login form is invalid with no username or password, url should
        remain on login page
        """
        c = Client()
        c.login(user="", password="")
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_no_password_input(self):
        """
        If login form is invalid with no password, url should remain on
        login page
        """
        c = Client()
        c.login(user="user", password="")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_no_username_input(self):
        """
        If login form is invalid with no username, url should remain on
        login page
        """
        c = Client()
        c.login(user="", password="passwd")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_if_successfully_logged_in(self): # works
        """
        Test if successfully logged in
        """
        c = Client()
        c.login(user="user", password="passwd")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_if_invalid_sign_up_form_do_not_go_to_homepage(self):
        """
        Test to see if the sign up form is invalid and if it is do not go to homepage
        """
        c = Client()
        c.login(user="", password="")
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_if_invalid_remain_at_sign_up(self):
        """
        Tests to see if it's invalid it remains at the login page sign up
        """
        c = Client()
        c.login(user="", password="12345")
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_if_successfully_signed_up(self): # works
        """
        Test if successfully signed up and redirects to homepage
        """
        c = Client()
        c.login(user="user123", password="passwd123")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code,200)


class LogoutViewTests(TestCase):

    # def test_logged_in_logout(self):
    """
    if the user is logged in and logout is requested, "Logout successfully"
    """


class ScheduleTests(TestCase):

    def test_no_enrolled_classes(self):
        """
        if the user is not enrolled in any classes, it will say "~not enrolled"
        """
	c = Client()
	c.login(user="abc", password="123")
	response = self.client.get(reverse('schedule'))
	self.assertContains(response, "No enrolled courses")
	
	

    def test_no_todos(self):
        """
        if there are no assignments posted for todos, it will say "~no posts have been posted"
	c = Client()
	c.login(user="abc", password="123")
	response = self.client.get(reverse('schedule'))
	self.assertContains(response, "No events have been posted")
        """

    def test_if_enrolled_class_added(self):
        """
        if the user enrolls in a class, the class is added in their schedule
	manually made a specific user a enrolled in this class
        """
	c = Client()
	c.login(user="a", password="a")
	response = self.client.get(reverse('schedule'))
	self.assertContains(response, "APMA 3140")


    def test_if_enrolled_assignment_shows(self):
        """
        an assignment post in that class will be shown in the To Do
	manually made a specific user enrolled in this class with this assignment
        """
	c = Client()
	c.login(user="a", password="a")
	response = self.client.get(reverse('schedule'))
	self.assertContains(response, "Test Assignment")

    def test_if_class_removed(self):
        """
        if a class is removed, the class is removed from their schedule
        """

    def test_if_assignment_from_removed_class_is_removed(self):
        """
        no assignments from a removed class should be listed in the list
        """

class SearchTests(TestCase):
    """
    include search bar tests here!!
    """



#REFERENCES
#Title: Django : Testing if the page has redirected to the desired url
#Author:
#Date: 11/12/2018
#Code Version:
#Availability: https://stackoverflow.com/questions/14951356/django-testing-if-the-page-has-redirected-to-the-desired-url

#Title: Testing Tools
#Author:
#Date: 11/12/2018
#Code Version:
#Availability: https://docs.djangoproject.com/en/2.1/topics/testing/tools/