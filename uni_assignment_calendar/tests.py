from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Events
import datetime
from datetime import timedelta
from django.utils.timezone import now
from django.test import Client


# helper functions -- need to edit
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

# ------------------------------------------------------------------------------------------

# Testing Model View -- these tests are okay!
# class AssignmentnModelTests(TestCase):
#
#     def test_was_published_recently_with_future_events(self):
#         """
#         was_published_recently() returns False for events whose pub_date
#         is in the future.
#         """
#         time = now() + timedelta(days=30)
#         future_question = Events(pub_date=time)
#         self.assertIs(future_question.was_published_recently(), False)
#
#     def test_was_published_recently_with_old_events(self):
#         """
#         was_published_recently() returns False for events whose pub_date
#         is older than 1 day.
#         """
#         time = now() - timedelta(days=1, seconds=1)
#         old_question = Events(pub_date=time)
#         self.assertIs(old_question.was_published_recently(), False)
#
#     def test_was_published_recently_with_recent_events(self):
#         """
#         was_published_recently() returns True for events whose pub_date
#         is within the last day.
#         """
#         time = now() - timedelta(hours=23, minutes=59, seconds=59)
#         recent_question = Events(pub_date=time)
#         self.assertIs(recent_question.was_published_recently(), True)

# ------------------------------------------------------------------------------------------
# Testing Index View
class AssignmentIndexViewTests(TestCase):
    def test_no_assignments(self): # works
        """
        If no post exist for any enrolled classes, an appropriate message is displayed.
        """
        response = self.client.get(reverse('index'))
        # self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events have been posted.")

    # def test_past_pub_date_events(self): # works
    #     """
    #     post with a pub_date in the past are displayed on the
    #     index page.
    #     """
    #     create_event_pub_date(events_name="Past Event.", pub_date=-30)
    #     response = self.client.get(reverse('index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_events_list'],
    #         ['<Events: Past Event.>']
    #     )
    #
    # def test_future_due_date_events(self): # works
    #     """
    #     post with a valid due date includes due date when posted on the index page
    #     """
    #     create_event_due_date(events_name="Future Due Date Event.", due_date=30)
    #     response = self.client.get(reverse('index'))
    #     self.assertQuerysetEqual(
    #         response.context['latest_events_list'],
    #         ['<Events: Future Due Date Event.>']
    #     )

    def test_redirects_to_create_page_if_logged_in(self):
        """
        tests if the "Post an Assignment" button redirects to the create page
        """
        c = Client()
        c.login(user="a", password="a")
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)

    def test_does_not_redirect_to_create_page_if_not_logged_in(self):
        """
        tests if the "Post an Assignment" button redirects to the create page
        """
        c = Client()
        c.login(user="a",password="a")
        c.logout()
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code == "200", False)

# ------------------------------------------------------------------------------------------
# Testing detail view
# class AssignmentDetailViewTests(TestCase):
#     def test_past_events(self): # works
#         """
#         The detail view of an event with a pub_date in the past
#         returns a 200.
#         """
#         past_events = create_event_pub_date(events_name="Past Published Date Event.", pub_date=30)
#         url = reverse('detail', args=(past_events.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#     def test_future_due_date_events(self): # works
#         """
#         The detail view of an event with a due_date in the future
#         returns a 200.
#         """
#         future_events = create_event_due_date(events_name="Future Due Date Event.", due_date=30)
#         url = reverse('detail', args=(future_events.id,))
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

# ------------------------------------------------------------------------------------------

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
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_no_username_input(self):
        """
        If login form is invalid with no username, url should remain on
        login page
        """
        c = Client()
        c.login(user="", password="passwd")
        response = self.client.get(reverse('login'))
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

    def test_logged_in_logout(self):
        """
        if the user is logged in and logout is requested, "Logout successfully"
        """
        c = Client()
        c.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class ScheduleTests(TestCase):

    def test_no_enrolled_classes(self): # works
        """
        if the user is not enrolled in any classes, it will say "~not enrolled"
        """
        c = Client()
        c.login(user="abc", password="123")
        response = self.client.get(reverse('schedule'))
        self.assertContains(response, "No enrolled courses.")

    def test_if_enrolled_in_courses(self):
        c = Client()
        c.login(user="abc", password="123")
        response = self.client.get(reverse('schedule'))
        self.assertContains(response, "No enrolled courses.")


class LoggedOutView(TestCase):
    def test_goals(self):
        """
        tests goals page
        """
        c = Client()
        response = self.client.get(reverse('goals'))
        self.assertContains(response, "Goals")

    def test_about_us(self):
        """
        tests about us page
        """
        c = Client()
        response = self.client.get(reverse("AboutUs"))
        self.assertContains(response,"About Us")


    def test_sign_up(self):
        """
        tests sign up page
        """
        c = Client()
        response = self.client.get(reverse("signup"))
        self.assertContains(response,"Sign Up")





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
#Title: Testing Tools
#Author:
#Date: 11/12/2018
#Code Version:
#Availability: https://docs.djangoproject.com/en/2.1/topics/testing/tools/
#HTTP 302
#Date: 12/10/2018
#Availability: https://en.wikipedia.org/wiki/HTTP_302
