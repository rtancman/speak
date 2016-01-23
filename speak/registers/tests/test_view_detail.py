from django.test import TestCase
from speak.registers.models import Register

class DetailGet(TestCase):
    def setUp(self):
        self.obj = Register.objects.create(
            name='Raffael Tancman',
            email='rtancman@gmail.com'
        )
        self.resp = self.client.get('/cadastro/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'registers/register_detail.html')