from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return render(request, 'registers/register_form.html')