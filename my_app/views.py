from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from predict.main import Robot
import gc
import asyncio
import ccxt
import pandas as pd

def index(request):
    try:
        return render(request,'index.html',{'robots':asyncio.get_event_loop()})
    except:
        return render(request,'index.html',{'robots':"none"})

def startRobot(request, strategy, ammount):
    robotInstance = Robot(strategy, ammount)
    robotInstance.start()
    return HttpResponse(f"ligou {robotInstance}")

def stopRobot(request):
    for obj in gc.get_objects():
        if isinstance(obj, Robot):
            name = obj.__str__()
            del obj
    return HttpResponse(f"desligou {name}")
