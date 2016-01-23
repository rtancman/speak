from django.test import TestCase
from speak.registers.forms import RegisterForm
from speak.registers.models import Register

class RegisterGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'registers/register_form.html')

    def test_html(self):
        tags = (('<form',1),
                ('type="text"',1),
                ('type="email"',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RegisterForm)

class RegisterPostValid(TestCase):
    def setUp(self):
        data = dict(name= 'Raffael Tancman', email= 'rtancman@gmail.com')
        self.resp = self.client.post('/cadastro/', data)

    def test_post(self):
        self.assertRedirects(self.resp, '/cadastro/1/')

    def test_save(self):
        self.assertTrue(Register.objects.exists())

class RegisterPostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/cadastro/', {})

    def test_post(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'registers/register_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, RegisterForm)

    def test_form_has_erros(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save(self):
        self.assertFalse(Register.objects.exists())