from apscheduler.schedulers.blocking import BlockingScheduler
from django.core import management

sched = BlockingScheduler()
print('Iniciando scheduler...')

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    try:
        print("Apagando e Reinserindo Dados Atualizados...")
        management.call_command('flush_update_db', verbosity=3)
    except Exception as e:
        print(e)

#@sched.scheduled_job('cron', day_of_week='mon-fri', hour=17, minute=22)
#def scheduled_job():
#    print('This job is run every weekday at 5:20pm.')

sched.start()
