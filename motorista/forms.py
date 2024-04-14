from django import forms


from .models import Motorista

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = ('cod_motorista', 'nome', 'telefone', 'cnh')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cod_motorista'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Id do motorista',
        })
        self.fields['nome'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Nome do motorista',
        })
        self.fields['telefone'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'Telefone do motorista',
        })
        self.fields['cnh'].widget.attrs.update({
            'class': 'input input-bordered w-full',
            'placeholder': 'CNH do motorista',
            })