"""Platzigram Views"""

from django.http import HttpResponse,JsonResponse
# Utilities
from datetime import datetime
import json

def hello_world(request):
    """Return a Greeting"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse("Ohh, hi! Current time server is {now}".format(now=str(now)))

def sort_integers(request):
    """Hi"""
    ingreso = request.GET['numbers'].split(",")
    lista = [ int(i) for i in ingreso]
    lista.sort()
    data = {
        'status' : 'ok',
        'numbers' : 'lista',
        'message' : 'Integers sorted succesfully!'
    }
    return JsonResponse(data)

def say_hi(request,name,age):
    """Return a freeting"""
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hello {}, Welcome to Platzigram !!!".format(name)
    return HttpResponse(message)