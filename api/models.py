from munch import Munch
from django.db import models

urls = {
    'camara': 'http://www.camara.gov.br/proposicoesWeb/fichadetramitacao?idProposicao=',
    'senado': 'https://www25.senado.leg.br/web/atividade/materias/-/materia/'
}


class Choices(Munch):
    def __init__(self, choices):
        super().__init__({i: i for i in choices.split(' ')})


class Proposicao(models.Model):

    id_ext = models.IntegerField(
        'ID Externo',
        help_text='Id externo do sistema da casa.')

    numero = models.IntegerField(
        'Número',
        help_text='Número da proposição naquele ano e casa.')

    sigla_tipo = models.CharField(
        'Sigla do Tipo', max_length=3,
        help_text='Sigla do tipo da proposição (PL, PLS etc)')

    data_apresentacao = models.DateField('Data de apresentação')

    casas = Choices('camara senado')
    casa = models.CharField(
        max_length=6, choices=casas.items(),
        help_text='Casa desta proposição.')

    regimes = Choices('ordinario prioridade urgencia')
    regime_tramitacao = models.CharField(
        'Regime de tramitação',
        max_length=10, choices=regimes.items(), null=True)

    formas_apreciacao = Choices('conclusiva plenario')
    forma_apreciacao = models.CharField(
        'Forma de Apreciação',
        max_length=10, choices=formas_apreciacao.items(), null=True)

    ementa = models.TextField(blank=True)

    justificativa = models.TextField(blank=True)

    palavras_chave = models.TextField(blank=True)

    casa_origem = models.TextField(blank=True)

    autor_nome = models.TextField(blank=True)

    energia = models.FloatField(null=True)

    em_pauta = models.NullBooleanField(help_text='TRUE se a proposicao estara em pauta na semana ou FALSE caso contrario')

    tema = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['casa', 'id_ext']),
        ]
        ordering = ('-data_apresentacao',)

    @property
    def sigla(self):
        '''Sigla da proposição (ex.: PL 400/2010)'''
        return f'{self.sigla_tipo} {self.numero}/{self.ano}'

    @property
    def ano(self):
        return self.data_apresentacao.year

    @property
    def url(self):
        '''URL para a página da proposição em sua respectiva casa.'''
        return urls[self.casa] + str(self.id_ext)

    @property
    def resumo_tramitacao(self):
        locais = []
        events = []
        for event in self.tramitacao.all():
            if event.sigla_local not in locais:
                locais.append(event.sigla_local)
                events.append({
                    'data': event.data,
                    'casa': event.proposicao.casa,
                    'nome': event.sigla_local
                })
        return events

        # return [{
        #     'data': i.data,
        #     'nome': i.sigla_local
        # } for i in self.tramitacao.all()]
        # return [i[0] for i in self.tramitacao.values_list('sigla_local').distinct()]


class TramitacaoEvent(models.Model):

    data = models.DateField('Data')

    sequencia = models.IntegerField(
        'Sequência',
        help_text='Sequência desse evento na lista de tramitações.')

    texto = models.TextField()

    sigla_local = models.TextField()

    situacao = models.TextField()

    proposicao = models.ForeignKey(
        Proposicao, on_delete=models.CASCADE, related_name='tramitacao')

    class Meta:
        ordering = ('sequencia',)
