from rest_framework import serializers, generics
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.model.ator import Atores
from api.utils.filters import get_filtered_interesses
from api.utils.peso_politico import (
    get_peso_politico_lista,
    get_peso_politico_parlamentar,
)


class PesoPoliticoSerializer(serializers.Serializer):
    idParlamentarVoz = serializers.IntegerField()
    pesoPolitico = serializers.FloatField()


class PesoPoliticoLista(generics.ListAPIView):
    """
    Informação sobre o peso político dos parlamentares.
    """

    serializer_class = PesoPoliticoSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "interesse",
                openapi.IN_PATH,
                "Interesse que se deseja obter a lista com os parlamentares e seus pesos políticos",
                type=openapi.TYPE_INTEGER,
            )
        ]
    )
    def get_queryset(self):
        """
        Retorna dados de peso político para os atores de um determinado interesse.
        Caso nenhum seja passado, o valor default será leggo.
        """
        interesse_arg = self.request.query_params.get("interesse")
        if interesse_arg is None:
            interesse_arg = "leggo"
        interesses = get_filtered_interesses(interesse_arg)

        lista_ids = list(
            Atores.objects.filter(id_leggo__in=interesses).values_list(
                "id_autor", flat=True
            )
        )

        # TODO: Remover a linha abaixo quando o mapeamento estiver concluído
        # data = get_peso_politico_lista([1, 23396, 173531])

        data = get_peso_politico_lista(lista_ids)

        return data


class PesoPoliticoParlamentar(generics.ListAPIView):
    """
    Informação sobre o peso político dos parlamentares.
    """

    serializer_class = PesoPoliticoSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "id",
                openapi.IN_PATH,
                "Id do autor que se deseja saber o peso político",
                type=openapi.TYPE_INTEGER,
            )
        ]
    )
    def get_queryset(self):
        """
        Retorna dados de peso político para os atores de um determinado interesse.
        Caso nenhum seja passado, o valor default será leggo.
        """
        id_autor_arg = self.kwargs["id"]

        id = (
            Atores.objects.filter(id_autor=id_autor_arg)
            .values_list("id_autor", flat=True)
            .first()
        )

        # TODO: Remover a linha abaixo quando o mapeamento estiver concluído
        # id = 1204467

        data = get_peso_politico_parlamentar(id)

        return data
