from django.test import TestCase


class RegisterTestGet(TestCase):
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
