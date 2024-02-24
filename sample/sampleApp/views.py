from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from .tasks import addToCache

# Create your views here.
def index(request):
    addToCache.delay()
    return HttpResponse("Hello, world. You're at the polls index.")


def getCache(request):
    x = cache.get('test')
    return JsonResponse({'test': x})