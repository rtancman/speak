from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from speak.registers.forms import RegisterForm
from speak.registers.models import Register


def register(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = RegisterForm(request.POST)

    if not form.is_valid():
        return render(request, 'registers/register_form.html',
                      {'form': form})

    register = Register.objects.create(**form.cleaned_data)

    return HttpResponseRedirect('/cadastro/{}/'.format(register.pk))

def new(request):
    return render(request, 'registers/register_form.html',
                  {'form': RegisterForm()})

def detail(request, pk):
    try:
        register = Register.objects.get(pk=pk)
    except Register.DoesNotExist:
        raise Http404

    return render(request, 'registers/register_detail.html', {'register': register} )