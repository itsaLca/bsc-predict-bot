from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
from predict.main import Robot
import gc

def index(request):
    robots = []
    for obj in gc.get_objects():
        if isinstance(obj, Robot):
            robots.push(obj)
    return render(request,'index.html',{'robots':robots})

def startRobot(request, strategy, ammount):
    robotInstance = Robot(strategy, ammount)
    robotInstance.start()

def stopRobot(request):
    for obj in gc.get_objects():
        if isinstance(obj, Robot):
            del obj
