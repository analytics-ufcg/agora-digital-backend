# Generated by Django 3.0 on 2019-12-03 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0070_auto_20191122_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='etapaproposicao',
            name='advocacy_link',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proposicao',
            name='advocacy_link',
            field=models.TextField(blank=True, null=True),
        ),
    ]