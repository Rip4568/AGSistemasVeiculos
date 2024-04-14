from django.contrib import admin

from carro.models import Veiculo
from motorista.models import Motorista
from controle.models import ControleRegistro
    
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'km_troca_oleo')
    list_filter = ('placa', 'marca', 'km_troca_oleo')
    list_editable = ('km_troca_oleo',)

admin.site.register(Veiculo, VeiculoAdmin)

class MotoristaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cnh')
    list_display_links = ('nome', 'cnh')
    list_filter = ('nome', 'cnh')

admin.site.register(Motorista, MotoristaAdmin)

class ControleRegistroAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'motorista', 'destino', 'saida', 'retorno', 'km_pecorrido')
    list_display_links = ('veiculo', 'motorista', 'destino', 'saida', 'retorno', 'km_pecorrido')
    list_filter = ('veiculo', 'motorista', 'destino', 'saida', 'retorno', 'km_pecorrido')
    list_editable = ('destino', 'km_pecorrido')

admin.site.register(ControleRegistro)