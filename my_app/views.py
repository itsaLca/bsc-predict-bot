from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from predict.main import Robot
import gc
import asyncio
import ccxt
import panda as pd
def index(request):
    try:
        return render(request,'index.html',{'robots':asyncio.all_tasks()})
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

def test(request):
    binance = ccxt.binance()
    bars = binance.fetch_ohlcv('BTC/USDT','1d',limit=100)
    for line in bars:
    del line[5:]
    #  2 dimensional tabular data
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])   
    return HttpResponse(df)
        # cryptoaux.get_crypto_data("BUSD/USDT", "2021-01-08", "2021-01-08"))