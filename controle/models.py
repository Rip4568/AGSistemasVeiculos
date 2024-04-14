from typing import Iterable
from django.db import models
from django.utils.timezone import localtime

from carro.models import Veiculo
from motorista.models import Motorista

class ControleRegistro(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.DO_NOTHING, blank=False, null=False, related_name='registros')
    motorista = models.ForeignKey(Motorista, on_delete=models.DO_NOTHING, blank=False, null=False, related_name='registros')
    destino = models.CharField('Destino', max_length=50, blank=False, null=False)
    saida = models.DateTimeField('Data e hora da Saida', blank=False, null=False)
    retorno = models.DateTimeField('Data e hora do Retorno', blank=True, null=True)
    km_saida = models.IntegerField('Km Saida', default=0)
    km_retorno = models.IntegerField('Km Retorno', default=0)
    km_pecorrido = models.IntegerField('Km Percorrido (campo sera calculado automaticamente apos salvar)', default=0)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    def save(self, *args, **kwargs):
        self.km_pecorrido = self.km_retorno + self.km_saida
        self.veiculo.km_troca_oleo -=  self.km_pecorrido
        self.veiculo.save()
        super(ControleRegistro, self).save(*args, **kwargs)
    
    @property
    def created_at_region(self):
        return localtime(self.created_at).strftime('%d/%m/%Y %H:%M')
    
    @property
    def updated_at_region(self):
        return localtime(self.updated_at).strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return f"{self.veiculo} | {self.motorista} | {self.km_pecorrido}"

    class Meta:
        db_table = 'controle_registros'
        managed = True
        verbose_name = 'ControleRegistro'
        verbose_name_plural = 'ControleRegistros'
