from django.test import TestCase

# Create your tests here.
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core import management

import mysite.models as models

class LoginRedirect(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        management.call_command('create_user', username='admin', password='secret')

    
    def test_login_redirect(self):
        """
        Test that the login page redirects to the home page after a successful login
        """
        response = self.client.post(reverse_lazy('login'), {'username': 'admin', 'password': 'secret'}, follow=True)
        self.assertRedirects(response, reverse_lazy('home'))
