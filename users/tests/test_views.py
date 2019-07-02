from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='John',
            email='johndoe@gmail.com',
            password='password1234'
        )

    def test_login(self):
        self.client.login(username='John', password='password1234')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_profile_page(self):
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_show_favs_page(self):
        response = self.client.get(reverse('show_favs'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/contact.html')

    def test_mentions_page(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/mentions.html')
