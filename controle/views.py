import json
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
    return redirect('controle:home')

def render_form_update_controle_registro(request: HttpRequest, pk: int) -> HttpResponse:
    controle = ControleRegistro.objects.get(pk=pk)
    form = ControleRegistroForm(instance=controle)
    context = {
        'form': form,
        'registro': controle
    }
    return HttpResponse(loader.render_to_string(
        'controle/layouts/_form_controle.html',
        context,
        request=request))
    
    
def render_table_list_controle_registro(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        data = json.loads(request.body)
        filtrar_data_registro = data.get('filtrar-data-registro')
        
        registros = ControleRegistro.objects.filter(
            saida__icontains=filtrar_data_registro
        ).select_related(
            'veiculo', 
            'motorista'
        ).order_by('-saida')
        context = {
            'registros': registros
        }
        return HttpResponse(loader.render_to_string(
            'controle/layouts/_table_list_controle.html',
            context,
            request=request))
    return HttpResponse('Metodo não aceito')