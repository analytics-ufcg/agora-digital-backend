# Generated by Django 2.2.5 on 2019-09-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0056_proposicao_advocacy_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapaproposicao',
            name='advocacy_link',
            field=models.TextField(blank=True),
        ),
    ]