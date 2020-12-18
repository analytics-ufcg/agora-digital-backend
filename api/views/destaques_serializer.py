from rest_framework import serializers, generics
from django.db.models import Q
from api.model.destaques import Destaques
from api.views.interesse_serializer import InteresseSerializer
from api.views.etapa_serializer import EtapasSerializer
from api.model.proposicao import Proposicao


class DestaquesDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Destaques
        fields = (
            "id_leggo", "criterio_aprovada_em_uma_casa", "casa_aprovacao",
            "data_aprovacao", "criterio_avancou_comissoes", 
            "comissoes_camara", "comissoes_senado")


class DestaquesSerializer(serializers.ModelSerializer):
    etapas = EtapasSerializer(many=True, read_only=True)
    interesse = InteresseSerializer(many=True, read_only=True)

    class Meta:
        model = Proposicao
        fields = (
            "id",
            "interesse",
            "etapas",
            "id_leggo",
            "sigla_camara",
            "sigla_senado",
            "destaques"
        )


class DestaquesList(generics.ListAPIView):

    serializer_class = DestaquesDetailsSerializer

    def get_queryset(self):

        props = (Destaques.objects.filter(
            Q(criterio_aprovada_em_uma_casa=True) |
            Q(criterio_avancou_comissoes=True))
        )

        return props


"""
        interesseArg = self.request.query_params.get("interesse")
        if interesseArg is None:
            interesseArg = "leggo"
        interessesFiltered = get_filtered_interesses(interesseArg)
        retorno = (Proposicao.objects.filter(interesse__interesse=interesseArg)
            .distinct()
            .prefetch_related(
                "etapas",
                "progresso",
                Prefetch("etapas__relatoria"),
                Prefetch("interesse", queryset=interessesFiltered),
                Prefetch("destaques", queryset=props)
            )) """
