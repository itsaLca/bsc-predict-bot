from django.shortcuts import render
from . import calculo1
from . import mt5
from datetime import datetime
from django.views.generic.base import TemplateView

def calculo(request, data):
    calcData = calculo1.calc(data.replace('-','/'))
    return render(request,'calculo1.html',{'dia':data,'pontos':calcData['pontos'],'calculo1':calcData['calculo1']})

def index(request):
    data =  data=datetime.today().strftime('%d/%m/%Y')
    calcData = calculo1.calc(data)
    return render(request,'index.html',{'dia':data,'pontos':calcData['pontos'],'calculo1':calcData['calculo1']})

def metatrader(request):
    return render(request,'metatrader.html',{'res': mt5.calc()})
