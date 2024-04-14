from django import forms


from .models import Veiculo

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ('placa', 'marca', 'km_troca_oleo', 'veiculo')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['placa'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Placa do carro',
            })
        self.fields['marca'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Marca do carro',
            })
        self.fields['km_troca_oleo'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Km para troca do oleo',
            'min': 0
            })
        self.fields['veiculo'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Tipo de Veiculo',
            })