# Generated by Django 2.1.2 on 2018-10-17 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20181010_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progresso',
            name='data_fim',
            field=models.DateField(blank=True, null=True, verbose_name='Data final'),
        ),
        migrations.AlterField(
            model_name='progresso',
            name='data_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Data de início'),
        ),
        migrations.AlterField(
            model_name='progresso',
            name='local',
            field=models.TextField(blank=True, null=True),
        ),
    ]
