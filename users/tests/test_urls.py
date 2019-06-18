from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, favs, defavs, show_favs, profile, mentions, contact


class TestUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_favs_url_resolves(self):
        url = reverse('favorite_product')
        self.assertEquals(resolve(url).func, favs)

    def test_defavs_sim_url_resolves(self):
        url = reverse('defavorite_product')
        self.assertEquals(resolve(url).func, defavs)

    def test_show_favs_url_resolves(self):
        url = reverse('show_favs')
        self.assertEquals(resolve(url).func, show_favs)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)

    def test_mentions_url_resolves(self):
        url = reverse('mentions')
        self.assertEquals(resolve(url).func, mentions)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func, contact)


