# Generated by Django 2.2.7 on 2019-11-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_merge_20191119_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoria',
            name='coautores',
            field=models.TextField(default='', help_text='Todos coautores de um documento.'),
            preserve_default=False,
        ),
    ]
