from django import forms
from .models import ControleRegistro

class ControleRegistroForm(forms.ModelForm):
    class Meta:
        model = ControleRegistro
        fields = ['veiculo', 'motorista', 'destino', 'saida', 'retorno', 'km_saida', 'km_retorno']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'input input-bordered w-full'}),
            'motorista': forms.Select(attrs={'class': 'input input-bordered w-full'}),
            'destino': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'saida': forms.DateTimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'date'}),
            'retorno': forms.DateTimeInput(attrs={'class': 'input input-bordered w-full', 'type': 'date'}),
            'km_saida': forms.TextInput(attrs={
                'class': 'input input-bordered w-full', 
                'type': 'number', 
                'step': '1', 
                'min': '0'
            }),
            'km_retorno': forms.TextInput(attrs={
                'class': 'input input-bordered w-full', 
                'type': 'number',
                'step': '1',
                'min': '0'
            }),
        }