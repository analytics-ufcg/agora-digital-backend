# Generated by Django 2.1.7 on 2019-08-16 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_atores_tipo_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pressao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Dia da popularidade')),
                ('max_pressao_principal', models.IntegerField(verbose_name='Pressão do nome formal e do apelido')),
                ('max_pressao_rel', models.IntegerField(verbose_name='Pressão dos termos relacionados')),
                ('maximo_geral', models.IntegerField(verbose_name='Pressão dos termos relacionados')),
                ('proposicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pressao', to='api.EtapaProposicao')),
            ],
        ),
    ]
