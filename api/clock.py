from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import management
import os
import django
import time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agorapi.settings")
django.setup()

sched = BlockingScheduler()
print('Iniciando scheduler...')

@sched.scheduled_job('interval', minutes=2)
def timed_job():
    try:
        print("Apagando Banco de Dados...")
        management.call_command('flush', '--no-input',verbosity=3)
        time.sleep(30)
        print("Fazendo Migrations...")
        management.call_command('makemigrations', verbosity=3)
        time.sleep(20)
        print("Rodando Migrations...")
        management.call_command('migrate',verbosity=3)
        time.sleep(20)
        print("Importando dados a partir de servidor remoto...")
        management.call_command('import_data_from_remote', verbosity=3)
    except Exception as e:
        print(e)

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17, minute=22)
#def scheduled_job():
#    print('This job is run every weekday at 5:20pm.')

sched.start()
