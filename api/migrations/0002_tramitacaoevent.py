# Generated by Django 2.1 on 2018-09-04 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TramitacaoEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('sequencia', models.IntegerField(help_text='Sequência desse evento na lista de tramitações.', verbose_name='Sequência')),
                ('texto', models.TextField()),
                ('sigla_local', models.TextField()),
                ('situacao', models.TextField()),
                ('proposicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Proposicao')),
            ],
        ),
    ]