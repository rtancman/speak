from django.test import TestCase


class RegisterTestGet(TestCase):
    def test_get(self):
        resp = self.client.get('/cadastro/')
        self.assertEqual(200, resp.status_code)