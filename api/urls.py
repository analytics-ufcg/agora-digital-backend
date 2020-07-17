from django.conf.urls import url  # , include

# from rest_framework.routers import DefaultRouter
from api.views.info_serializer import Info
from api.views.proposicao_serializer import ProposicaoDetail, ProposicaoList
from api.views.etapa_serializer import EtapasList
from api.views.tramitacao_serializer import TramitacaoEventList
from api.views.progresso_serializer import ProgressoList
from api.views.comissao_serializer import ComissaoList
from api.views.pauta_serializer import PautaList
from api.views.emenda_serializer import EmendasList
from api.views.ator_serializer import (
    AtoresAgregadosList,
    AtoresProposicaoList,
    AtoresRelatoriasList,
    AtoresRelatoriasDetalhada,
    AtorList,
)
from api.views.pressao_serializer import PressaoList
from api.views.coautoria_node_serializer import CoautoriaNodeList
from api.views.coautoria_edge_serializer import CoautoriaEdgeList
from api.views.autoria_serializer import (AutoriaList,
                                          AutoriasAgregadasList,
                                          AutoriasAutorList)
from api.views.interesse_serializer import InteresseList
from api.views.anotacao_serializer import (
    AnotacaoListByProp,
    AnotacaoList,
    AnotacaoGeralList
)
from api.views.temperatura_historico_serializer import TemperaturaMaxPeriodo
from api.views.presidencia_comissao_serializer import PresidenciaComissaoLista, PresidenciaComissaoParlamentar
from api.views.peso_politico_serializer import PesoPoliticoLista, PesoPoliticoParlamentar
from api.views.autoria_serializer import AutoriasAgregadasByAutor


# router = DefaultRouter()
# router.register(r'proposicoes', views.ProposicaoViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^info/?$', Info.as_view()),
    url(r'^proposicoes/(?P<id>[0-9]+)/?$',
        ProposicaoDetail.as_view()),
    url(r'^proposicoes/?$', ProposicaoList.as_view()),
    url(r'^etapas/?$', EtapasList.as_view()),
    url(r'^eventos_tramitacao/(?P<casa>[a-z]+)/(?P<id_ext>[0-9]+)/?$',
        TramitacaoEventList.as_view()),
    url(r'^eventos_tramitacao/?$', TramitacaoEventList.as_view()),
    url(r'^proposicoes/(?P<id_ext>[0-9]+)/fases/?$', Info.as_view()),
    url(r'^progresso/(?P<casa>[a-z]+)/(?P<id_ext>[0-9]+)/?$',
        ProgressoList.as_view()),
    url(r'^comissao/(?P<casa>[a-z]+)/(?P<sigla>([a-z]+|[A-Z]+)[0-9]*)/?$',
        ComissaoList.as_view()),
    url(r'^pauta/(?P<casa>[a-z]+)/(?P<id_ext>[0-9]+)/?$',
        PautaList.as_view()),
    url(r'^emenda/(?P<casa>[a-z]+)/(?P<id_ext>[0-9]+)/?$',
        EmendasList.as_view()),
    url(r'^ator/(?P<id_autor>[0-9]+)/?$',
        AtorList.as_view()),
    url(r'^atores/(?P<id_leggo>[0-9]+)/?$',
        AtoresProposicaoList.as_view()),
    url(r'^atores/relatorias/?$',
        AtoresRelatoriasList.as_view()),
    url(r'^atores/agregados/?$',
        AtoresAgregadosList.as_view()),
    url(r'^atores/relatorias/detalhada/(?P<id_autor>[0-9]+)/?$',
        AtoresRelatoriasDetalhada.as_view()),
    url(r'^pressao/(?P<id_leggo>[0-9]+)/?$',
        PressaoList.as_view()),
    url(r'^coautorias_node/(?P<id>[0-9]+)/?$',
        CoautoriaNodeList.as_view()),
    url(r'^coautorias_edge/(?P<id>[0-9]+)/?$',
        CoautoriaEdgeList.as_view()),
    url(r'^autorias/(?P<id>[0-9]+)/?$',
        AutoriaList.as_view()),
    url(r'^ator/(?P<id_autor>[0-9]+)/autorias/?$',
        AutoriasAutorList.as_view()),
    url(r'^autorias/agregadas/?$',
        AutoriasAgregadasList.as_view()),
    url(r'^autorias/agregadas/(?P<id_autor>[0-9]+)/?$',
        AutoriasAgregadasByAutor.as_view()),
    url(r'^interesses/(?P<id>[0-9]+)/?$',
        InteresseList.as_view()),
    url(r'^anotacoes/?$',
        AnotacaoList.as_view()),
    url(r'^anotacoes/(?P<id>[0-9]+)/?$',
        AnotacaoListByProp.as_view()),
    url(r'^anotacoes-gerais/?$',
        AnotacaoGeralList.as_view()),
    url(r'^temperatura/max/?$',
        TemperaturaMaxPeriodo.as_view()),
    url(r'^comissao/presidencia/?$',
        PresidenciaComissaoLista.as_view()),
    url(r'^comissao/presidencia/(?P<id>[0-9]+)/?$',
        PresidenciaComissaoParlamentar.as_view()),
    url(r'^atores/peso_politico/?$',
        PesoPoliticoLista.as_view()),
    url(r'^atores/peso_politico/(?P<id>[0-9]+)/?$',
        PesoPoliticoParlamentar.as_view())
]
