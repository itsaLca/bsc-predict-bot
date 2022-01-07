from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
from predict.main import Robot

def index(request):
    data =  data=datetime.today().strftime('%d/%m/%Y')
    calcData = "oi"
    return render(request,'index.html',{'dia':data})

def startRobot(request, strategy, ammount):
    robotInstance = Robot(strategy, ammount)
    robotInstance.start()

def stopRobot(request):
    