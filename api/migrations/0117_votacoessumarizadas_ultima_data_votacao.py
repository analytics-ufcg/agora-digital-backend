# Generated by Django 3.1.4 on 2021-03-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0116_votacoessumarizadas_casa'),
    ]

    operations = [
        migrations.AddField(
            model_name='votacoessumarizadas',
            name='ultima_data_votacao',
            field=models.TextField(help_text='Data da última votação', null=True),
        ),
    ]
