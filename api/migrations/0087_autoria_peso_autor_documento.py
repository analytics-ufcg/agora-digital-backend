# Generated by Django 3.0.7 on 2020-07-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0086_merge_20200624_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoria',
            name='peso_autor_documento',
            field=models.FloatField(help_text='Peso do autor no documento', null=True),
        ),
    ]