from django.db import models


class Register(models.Model):
    name = models.CharField('nome', max_length=100)
    email = models.EmailField('email')
    created_at = models.DateTimeField('criado em', auto_now_add=True)