from django.test import TestCase
from users.forms import UserRegisterForm


class TestForms(TestCase):

    def test_usercreation_form_valid_data(self):
        form = UserRegisterForm(data={
            'username': 'roger1',
            'email': 'roger@gmail.com',
            'password1': '123456Abc*',
            'password2': '123456Abc*'
        })

        self.assertTrue(form.is_valid())

    def test_usercreation_no_data(self):
        form = UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)

    def test_usercreation_wrong_email(self):
        form = UserRegisterForm(data={
            'username': 'roger1',
            'email': 'roger@gmail',
            'password1': '123456Abc*',
            'password2': '123456Abc*'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_usercreation_wrong_password(self):
        form = UserRegisterForm(data={
            'username': 'roger1',
            'email': 'roger@gmail.com',
            'password1': '123456Abc',
            'password2': '123456Abc*'
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
