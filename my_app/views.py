from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
from ../predict/main import Robot

def index(request):
    data =  data=datetime.today().strftime('%d/%m/%Y')
    calcData = "oi"
    return render(request,'index.html',{'dia':data})

def runCommand(request, strategy, ammount):
    robotInstace = Robot(strategy, ammount)