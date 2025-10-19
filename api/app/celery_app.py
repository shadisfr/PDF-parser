import os
from celery import Celery

broker_url = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
result_backend = os.getenv("CELERY_RESULT_BACKEND", "redis://redis:6379/0")

celery_app = Celery(
    "docproc",
    broker=broker_url,
    backend=result_backend,
)

celery_app.conf.update(
    task_track_started=True,
    result_expires=60 * 60 * 24,  # 24h
    broker_connection_retry_on_startup=True,
)
