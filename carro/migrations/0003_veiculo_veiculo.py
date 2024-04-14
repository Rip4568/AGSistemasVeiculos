# Generated by Django 5.0.4 on 2024-04-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carro', '0002_alter_veiculo_km_troca_oleo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='veiculo',
            field=models.CharField(choices=[('carro', 'Carro'), ('moto', 'Moto')], default='carro', max_length=50, verbose_name='Tipo de Veiculo'),
        ),
    ]
