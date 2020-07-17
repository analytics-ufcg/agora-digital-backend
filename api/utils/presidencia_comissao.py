import json
import requests

URL_PRESIDENCIA_COMISSAO = "https://perfil.parlametria.org/api/busca-parlamentar"


def get_comissao_parlamentar(listaComissoesPassadas):
    try:
        r = requests.get(url=URL_PRESIDENCIA_COMISSAO)
        data = json.loads(r.text)
        obj_arr = []
        countComissoes = 0

        for obj in data:
            for index in obj['parlamentarComissoes']:
                if(index['cargo'] == "Presidente" and index['infoComissao']['sigla'] in listaComissoesPassadas):
                    countComissoes += 1
                    obj_arr.append({
                        'id_comissao': index['idComissaoVoz'],
                        'id_autor': obj['idParlamentar'],
                        'id_autor_voz': obj['idParlamentarVoz'],
                        'info_comissao': index['infoComissao']['sigla'],
                        'quantidade_comissao_presidente': countComissoes
                    })
                    countComissoes = 0

        return obj_arr

    except Exception as e:
        print(e)
        return []

def get_comissao_parlamentar_id(id_parlamentar, listaComissoesPassadas):

    try:
        r = requests.get(url=URL_PRESIDENCIA_COMISSAO)
        data = json.loads(r.text)
        obj_arr = []
        countComissoes = 0

        for obj in data:
            if(obj['idParlamentarVoz'] == id_parlamentar):
                for index in obj['parlamentarComissoes']:
                    if(index['cargo'] == "Presidente" and index['infoComissao']['sigla'] in listaComissoesPassadas):
                        countComissoes += 1
                        obj_arr.append({
                            'id_comissao': index['idComissaoVoz'],
                            'id_autor': obj['idParlamentar'],
                            'id_autor_voz': obj['idParlamentarVoz'],
                            'info_comissao': index['infoComissao']['sigla'],
                            'quantidade_comissao_presidente': countComissoes
                        })
                        countComissoes = 0

        return obj_arr

    except Exception as e:
        print(e)
        return []
