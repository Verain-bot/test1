from sample.celery import app
from celery import shared_task
from django.core.cache import cache

@shared_task
def addToCache():
    x = cache.get('test', 0)
    cache.set('test', x+1)
    return x+1