from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

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
    return redirect('motorista:register_and_list_motorista')
