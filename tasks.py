from celery import Celery
import iron_celery
import time

celery = Celery('tasks')
celery.conf.update(
    #BROKER_URL='ironmq://<project_id>:<token>@',
    BROKER_URL='ironmq://53084c2a9a3b0800050000b8:oAVbXmHuf_Zs5b1hKPoW8iaTp74@',
    #BROKER_URL='redis://localhost:6379/0',
    BROKER_POOL_LIMIT=2,
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT = ['json'],
    CELERY_RESULT_BACKEND='redis://localhost:6379/0',
    #CELERY_RESULT_BACKEND='mongodb://alyssa:nugitrocks123@ds035498.mongolab.com:35498/celery',
    #CELERY_RESULT_BACKEND='mongodb://alyssa:nugitrocks123@oceanic.mongohq.com:10000/celery',
    # CELERY_MONGODB_BACKEND_SETTINGS = {
    #   'database': 'nugqueue',
    #   'taskmeta_collection': 'tasks',
    # }
)

@celery.task
def add(x, y):
    print('Celery task {0}, {1}'.format(x, y))
    time.sleep(1)
    return x + y
