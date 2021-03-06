from django.db import models
from api.model.proposicao import Proposicao


class TemperaturaHistorico(models.Model):
    '''
    Histórico de temperatura de uma proposição
    '''
    id_leggo = models.TextField(
        null=True,
        help_text='Id da proposição principal no leggo.')

    periodo = models.DateField('periodo')

    temperatura_periodo = models.IntegerField(
        help_text='Quantidade de eventos no período (semana).')

    temperatura_recente = models.FloatField(
        help_text='Temperatura acumulada com decaimento exponencial.')

    proposicao = models.ForeignKey(
        Proposicao, on_delete=models.CASCADE, related_name='temperatura_historico')

    class Meta:
        ordering = ('-periodo',)
        get_latest_by = '-periodo'
