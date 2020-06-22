import json
import requests

from api.utils.csv_servers import post_req

URL_PRESIDENCIA_COMISSAO = "https://perfil.parlametria.org/api/busca-parlamentar"


def get_comissao_parlamentar():
    try:
        r = requests.get(url=URL_PRESIDENCIA_COMISSAO)
        data = json.loads(r.text)
        obj_arr = []
        quant = 0
     
        for obj in data:
            for index in obj['parlamentarComissoes']:
                if( index['cargo'] == "Presidente"):
                    countComissoes += 1
                    obj_arr.append({
                        'idParlamentarVoz': obj['idParlamentarVoz'],
                        'idComissaoPresidencia': index['idComissaoVoz'],
                        'quantidadePresidenciaComissoes': countComissoes 
                        })
                    countComissoes = 0
        return obj_arr 
        
    except Exception as e: 
        print(e)
        return []

