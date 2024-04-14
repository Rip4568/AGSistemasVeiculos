from typing import Iterable
from django.db import models
from django.urls import reverse
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _

class VeiculoManager(models.Manager):
    def with_km_pecorrido_total(self):
        """
        Retorna uma QuerySet de Veiculos com um campo adicional 'km_pecorrido_total'
        que representa a soma total de km_pecorrido para todos os registros de controle
        relacionados a cada veículo.
        """
        return self.annotate(km_pecorrido_total=models.Sum('registros__km_pecorrido'))
 
class Veiculo(models.Model):
    placa = models.CharField('Placa', max_length=8, unique=True, blank=False, null=False, db_index=True)
    marca = models.CharField('Marca', max_length=50, blank=True, null=True)
    veiculo = models.CharField(_("Tipo de Veiculo"), choices=(('carro', 'Carro'), ('moto', 'Moto')), default='carro', max_length=50)
    km_troca_oleo = models.IntegerField('Km Troca Oleo', default=10_000)
    
    objects = VeiculoManager()
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    
    @property
    def created_at_region(self):
        return localtime(self.created_at).strftime('%d/%m/%Y %H:%M')
    
    @property
    def updated_at_region(self):
        return localtime(self.updated_at).strftime('%d/%m/%Y %H:%M')

    
    class Meta:
        db_table = 'veiculos'
        managed = True
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
    

    def __str__(self):
        return f"{self.placa} | {self.veiculo}"


    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

