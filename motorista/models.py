from django.db import models
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _

class Motorista(models.Model):
    cod_motorista = models.CharField(_("Codigo do motorista (o id ja é o suficiente)"), max_length=50, blank=True, null=True)
    nome = models.CharField(_("Nome do motorista"), max_length=128, db_index=True, blank=False, null=False)
    telefone = models.CharField(_("Telefone do motorista (whatsapp)"), max_length=64, blank=True, null=True)
    cnh = models.CharField(_("CNH do motorista"), max_length=64, unique=True, db_index=True, blank=False, null=False)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    @property
    def created_at_region(self):
        return localtime(self.created_at).strftime('%d/%m/%Y %H:%M')
    
    @property
    def updated_at_region(self):
        return localtime(self.updated_at).strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'motoristas'
        managed = True
        verbose_name = 'Mtorista'
        verbose_name_plural = 'Mtoristas'