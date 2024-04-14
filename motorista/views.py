from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from motorista.forms import MotoristaForm
from motorista.models import Motorista

def register_and_list_motorista(request: HttpRequest) -> HttpResponse:
    form = MotoristaForm
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
    motoristas = Motorista.objects.all()
    context = {
        "form": form,
        "motoristas": motoristas
    }
    return render(request, 'motorista/list_and_register_motorista.html', context)
