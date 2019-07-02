from django.test import TestCase, Client
from django.urls import reverse
from answer.models import Product
from django.contrib.auth.models import User
import json


class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='John',
            email='johndoe@gmail.com',
            password='password1234'
        )

    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_login(self):
        self.client.login(username='John', password='password1234')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_show_favs_page(self): # doesn't work, need products?
        response = self.client.get(reverse('show_favs'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'users/favs.html')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/contact.html')

    def test_mentions_page(self):
        response = self.client.get(reverse('mentions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/mentions.html')
