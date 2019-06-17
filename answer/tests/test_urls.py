from django.test import SimpleTestCase
from django.urls import reverse, resolve
from answer.views import index, app, app_sim, detail, search


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, index)

    def test_app_url_resolves(self):
        url = reverse('application')
        self.assertEquals(resolve(url).func, app)

    def test_app_sim_url_resolves(self):
        url = reverse('application_sim')
        self.assertEquals(resolve(url).func, app_sim)

    def test_search_url_resolves(self):
        url = reverse('search-products')
        self.assertEquals(resolve(url).func, search)

    def test_detail_url_resolves(self):
        url = reverse('detail', args=[1234])
        self.assertEquals(resolve(url).func, detail)


