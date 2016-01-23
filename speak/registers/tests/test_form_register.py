from django.test import TestCase
from speak.registers.forms import RegisterForm

class RegisterFormTest(TestCase):
    def setUp(self):
        self.form = RegisterForm()

    def test_form_has_fields(self):
        expected = ['name', 'email']
        self.assertSequenceEqual(expected, list(self.form.fields))