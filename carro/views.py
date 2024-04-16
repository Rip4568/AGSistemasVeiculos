from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from carro.forms import VeiculoForm
from carro.models import Veiculo

def register_new_car(request:HttpRequest) -> HttpResponse:
    form = VeiculoForm
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
    veiculos = Veiculo.objects.all()
    context = {
        "form": form,
        'veiculos': veiculos
    }
    return render(request, 'carro/register_car.html', context)

def delete_car(request:HttpRequest, pk:int) -> HttpResponse:
    veiculo = Veiculo.objects.get(pk=pk)
    veiculo.delete()
    return redirect('carro:register_new_car')

def update_car(request:HttpRequest, pk:int) -> HttpResponse:
    veiculo = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(instance=veiculo)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return redirect('carro:register_new_car')


def render_form_update_car(request:HttpRequest, pk:int) -> HttpResponse:
    veiculo = Veiculo.objects.get(pk=pk)
    form = VeiculoForm(instance=veiculo)
    context = {
        'form': form,
        'veiculo': veiculo
    }
    return HttpResponse(
        loader.render_to_string('carro/layouts/_form_car.html', context, request=request)
    )
    
def render_form_delete_car(request:HttpRequest, pk:int) -> HttpResponse:
    veiculo = Veiculo.objects.get(pk=pk)
    context = {
        'veiculo': veiculo
    }
    return HttpResponse(
        loader.render_to_string('carro/layouts/_content_delete_modal.html', context, request=request)
    )
