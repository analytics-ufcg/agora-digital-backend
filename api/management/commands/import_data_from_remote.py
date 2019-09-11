from django.core.management.base import BaseCommand
from django.conf import settings
from api.utils.csv_servers import (get_token, get_leggo_files)
from .import_utils import import_all_data


class Command(BaseCommand):
    help = 'Importa dados'

    def handle(self, *args, **options):
        try:
            print("Obtendo token do SERVER URL:" + settings.CSVS_SERVER_URL + "...")
            token = get_token(settings.CSVS_SERVER_URL, 
                        settings.CSVS_SERVER_USER, 
                        settings.CSVS_SERVER_PWD)
            print("Token:" + token)

            print("Obtendo arquivos csv do servidor remoto...")
            get_leggo_files(settings.CSVS_SERVER_URL, token, settings.CSVS_STORAGE_DIR)

            print("Inserindo novos dados no BD...")
            import_all_data()
        except Exception:
            print("Não foi possível atualizar os dados a partir dos csvs remotos. =(")