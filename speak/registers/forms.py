from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')