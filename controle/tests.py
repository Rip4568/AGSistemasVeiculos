from django.db.models import Sum
from django.test import TestCase

from carro.models import Veiculo
from controle.models import ControleRegistro
from motorista.models import Motorista

class TestControleRegistro(TestCase):
    def setUp(self) -> None:
        self.veiculo = Veiculo.objects.create(
            placa='AAA0000',
            marca='Fiat',
            km_troca_oleo=1000
        )
        self.motorista = Motorista.objects.create(
            cnh='12345678901',
            nome='João da Silva',
            telefone='11987654321',
            cod_motorista='123456'
        )
        self.controle = ControleRegistro.objects.create(
            veiculo=self.veiculo,
            motorista=self.motorista,
            destino='Sao Paulo',
            saida='2022-01-01 10:00:00',
            km_saida=500,
            km_retorno=500,
        )

    def test_veiculo_quantidade_registros(self, valor=1):
        self.assertEqual(self.veiculo.registros.count(), valor)

    def test_motorista_quantidade_registros(self, valor=1):
        self.assertEqual(self.motorista.registros.count(), valor)

    def test_veiculo_km_totais_rodados(self):
        km_totais_pecorridos = self.veiculo.registros.all().aggregate(km_totais=Sum('km_pecorrido'))['km_totais']
        self.assertEqual(km_totais_pecorridos, 1000)

        self.veiculo.km_troca_oleo -= km_totais_pecorridos
        self.assertEqual(self.veiculo.km_troca_oleo, 0)

    def test_veiculo_esta_valido_para_rodar(self):
        km_totais_pecorridos = self.veiculo.registros.all().aggregate(km_totais=Sum('km_pecorrido'))['km_totais']
        self.veiculo.km_troca_oleo -= km_totais_pecorridos
        self.assertEqual(self.veiculo.km_troca_oleo, 0)