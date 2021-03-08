# Generated by Django 3.1 on 2021-03-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0110_votacao_is_nominal'),
    ]

    operations = [
        migrations.AddField(
            model_name='tramitacaoevent',
            name='temperatura_evento',
            field=models.FloatField(blank=True, help_text='Temperatura do evento.', null=True),
        ),
        migrations.AddField(
            model_name='tramitacaoevent',
            name='temperatura_local',
            field=models.FloatField(blank=True, help_text='Temperatura do local do evento.', null=True),
        ),
    ]
