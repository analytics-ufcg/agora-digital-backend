from rest_framework import serializers, generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from api.model.pressao import Pressao


class PressaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressao
        fields = (
            'date', 'trends_max_pressao_principal',
            'trends_max_pressao_rel',	'trends_max_popularity',
            'twitter_mean_popularity', 'popularity')


class PressaoList(generics.ListAPIView):
    '''
    A partir do id da proposição no Sistema leggo recupera histório da pressão 
    com as informações da pesquisa no Google Trends e a popularidade da proposição
    no Twitter.
    '''

    serializer_class = PressaoSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id_leggo', openapi.IN_PATH, 'id da proposição no sistema',
                type=openapi.TYPE_INTEGER),
        ]
    )
    def get_queryset(self):
        '''
        Retorna a pressão
        '''

        interesseArg = self.request.query_params.get('interesse')

        # Adiciona interesse default
        if interesseArg is None:
            interesseArg = 'leggo'

        id_leggo = self.kwargs['id_leggo']
        queryset = Pressao.objects.filter(
            proposicao__id_leggo=id_leggo, interesse=interesseArg)

        return queryset
