from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Login')

    def test_login_view_post_valid(self):
        response = self.client.post(reverse('login'), {
            'login_type': 'super',
            'username': 'testuser',
            'password': 'testpass',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Logged in as testuser')

    def test_login_view_post_invalid(self):
        response = self.client.post(reverse('login'), {
            'login_type': 'super',
            'username': 'testuser',
            'password': 'wrongpass',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')
