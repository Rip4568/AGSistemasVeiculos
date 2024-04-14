from django.db import models
from django.urls import reverse
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

""" por padrão eu sempre instancio uma classe abstarata o AbstractUser antes de começar a desenolver
com o django, o motivo disso é pq assim qualquer campo que eu venha ter em adicional fica mais facil de 
implementar"""

class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    @property
    def created_at_region(self):
        return localtime(self.created_at).strftime('%d/%m/%Y %H:%M')
    
    @property
    def updated_at_region(self):
        return localtime(self.updated_at).strftime('%d/%m/%Y %H:%M')

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("User_detail", kwargs={"pk": self.pk})
