from django.test import TestCase, Client
from django.urls import reverse
from answer.models import Product
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_page(self):

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/index.html')

    def test_search_page(self):
        response = self.client.get(reverse('search-products'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/search.html')

    def test_app_page(self): # doesn't work
        response = self.client.get(reverse('application'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/results.html')
        self.assertTemplateUsed(response, 'answer/layout.html')
        self.assertTemplateUsed(response, 'answer/list.html')

    def test_app_sim_page(self): # doesn't work
        response = self.client.get(reverse('application_sim'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'answer/results.html')
