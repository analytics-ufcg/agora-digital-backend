# Generated by Django 3.1.4 on 2021-03-23 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0113_auto_20210316_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='VotacoesSumarizadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_parlamentar', models.IntegerField(help_text='Id do parlamentar', null=True)),
                ('id_parlamentar_parlametria', models.IntegerField(help_text='Id do parlamentar na plataforma parlametria', null=True)),
                ('num_votacoes_totais_governismo', models.IntegerField(help_text='Número de votações totais consideradas no governismo', null=True)),
                ('num_votacoes_totais_disciplina', models.IntegerField(help_text='Número de votações totais consideradas na disciplina partidária', null=True)),
                ('num_votacoes_parlamentar_governismo', models.IntegerField(help_text='Número de votações do parlamentar consideradas no governismo', null=True)),
                ('num_votacoes_parlamentar_disciplina', models.IntegerField(help_text='Número de votações do parlamentar consideradas na disciplina partidária', null=True)),
            ],
        ),
    ]
