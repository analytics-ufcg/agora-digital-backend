from django.db import models


class CoautoriaEdge(models.Model):
    '''
    Arestas para criação do grafo de coautorias
    '''
    id_leggo = models.TextField(
        help_text='Id do leggo.')

    source = models.IntegerField(
        help_text='Origem da aresta.')

    target = models.IntegerField(
        help_text='Destino da aresta.')

    value = models.TextField(
        help_text='Valor da aresta.')
