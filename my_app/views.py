from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
import subprocess
def index(request):
    data =  data=datetime.today().strftime('%d/%m/%Y')
    calcData = "oi"
    return render(request,'index.html',{'dia':data,'pontos':calcData,'calculo1':calcData})

def runCommand(request, strategy, size):
    cmd = f"python main.py --strategy {stategy} --size {size}"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()