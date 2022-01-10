from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from predict.main import Robot
import gc
import asyncio
import ccxt
import logging
import pandas as pd

def index(request):
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
    bars = binance.fetch_ohlcv('BNB/USDT','5m',limit=133)
    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close','vol'])
    dfC = df['close']
    sma50 = df['close'].rolling(50).mean()
    return HttpResponse([dfC.iloc[-1], sma50.iloc[-1]])

