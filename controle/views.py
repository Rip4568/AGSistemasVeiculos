from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from carro.models import Veiculo
from controle.forms import ControleRegistroForm
from controle.models import ControleRegistro
from motorista.models import Motorista

def home(request: HttpRequest) -> HttpResponse:
    form = ControleRegistroForm
    if request.method == 'POST':
        form = ControleRegistroForm(request.POST)
        if form.is_valid():
            form.save()
    registros = ControleRegistro.objects.all().select_related(
        'veiculo', 
        'motorista'
    ).order_by('-saida')
    veiulos = Veiculo.objects.all()
    motoristas = Motorista.objects.all()
    context = {
        'form': form,
        'registros': registros,
        'veiculos': veiulos,
        'motoristas': motoristas
    }
    return render(request, 'controle/index.html', context)


def delete_regisro_controle(request: HttpRequest, pk: int) -> HttpResponse:
    controle = ControleRegistro.objects.get(pk=pk)
    controle.delete()
    return redirect('controle:home')


def update_regisro_controle(request: HttpRequest, pk: int) -> HttpResponse:
    controle = ControleRegistro.objects.get(pk=pk)
    form = ControleRegistroForm(instance=controle)
    if request.method == 'POST':
        form = ControleRegistroForm(request.POST, instance=controle)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'controle/index.html', context)

def render_form_update_controle_registro(request: HttpRequest, pk: int) -> HttpResponse:
    controle = ControleRegistro.objects.get(pk=pk)
    form = ControleRegistroForm(instance=controle)
    context = {
        'form': form
    }
    return loader.render_to_string(
        'controle/layouts/_form_controle.html',
        context,
        request=request
    )
