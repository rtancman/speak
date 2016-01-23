from datetime import datetime

from django.test import TestCase
from speak.registers.models import Register


class RegisterModelTest(TestCase):
    def setUp(self):
        self.obj = Register(
            name= 'Raffael Tancman',
            email='rtancman@gmail.com'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Register.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)