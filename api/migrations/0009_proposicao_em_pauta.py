# Generated by Django 2.1.1 on 2018-09-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_proposicao_energia'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposicao',
            name='em_pauta',
            field=models.NullBooleanField(help_text='TRUE se a proposicao estara em pauta na semana ou FALSE caso contrario'),
        ),
    ]
