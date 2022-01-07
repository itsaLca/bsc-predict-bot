from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView

def index(request):
    data =  data=datetime.today().strftime('%d/%m/%Y')
    calcData = "oi"
    return render(request,'index.html',{'dia':data,'pontos':calcData,'calculo1':calcData})
