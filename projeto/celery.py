from celery import Celery
from datetime import timedelta
from django.conf import settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
app = Celery('projeto', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Adicione o suporte ao evento loop assíncrono do Celery
app.conf.worker_pool_restarts = True

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['application/json'],
    CELERY_TIMEZONE=settings.TIME_ZONE,
    CELERY_ENABLE_UTC=True,
    CELERY_RESULT_PERSISTENT=True,
    CELERY_TRACK_STARTED=True,
    CELERY_BROKER_CONNECTION_RETRY=True,
    CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP=True,
    CELERY_TASK_TIME_LIMIT=3100,  
    CELERY_TASK_SOFT_TIME_LIMIT=3100,
    CELERY_MAX_MEMORY_PER_CHILD = 500000,  # 500 MB
    CELERY_WORKER_CONCURRENCY=1,  # Número de trabalhadores
    CELERY_RESULT_EXTENDED = True
)