# Generated by Django 5.0.4 on 2024-04-13 16:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carro', '0001_initial'),
        ('motorista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ControleRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destino', models.CharField(max_length=50, verbose_name='Destino')),
                ('saida', models.DateTimeField(verbose_name='Saida')),
                ('retorno', models.DateTimeField(blank=True, null=True, verbose_name='Retorno')),
                ('km_saida', models.IntegerField(default=0, verbose_name='Km Saida')),
                ('km_retorno', models.IntegerField(default=0, verbose_name='Km Retorno')),
                ('km_pecorrido', models.IntegerField(default=0, verbose_name='Km Percorrido')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='motorista.motorista')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registros', to='carro.veiculo')),
            ],
            options={
                'verbose_name': 'ControleRegistro',
                'verbose_name_plural': 'ControleRegistros',
                'db_table': 'controle_registros',
                'managed': True,
            },
        ),
    ]
