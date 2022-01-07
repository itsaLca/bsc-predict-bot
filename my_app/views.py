from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
import subprocess
from django.http.response import StreamingHttpResponse
from queue import Queue, Empty
from threading import Thread, current_thread
import time
import sys


class Printer:
    def __init__(self):
        self.queues = {}

    def write(self, value):
        '''handle stdout'''
        queue = self.queues.get(current_thread().name)
        if queue:
            queue.put(value)
        else:
            sys.__stdout__.write(value)

    def flush(self):
        '''Django would crash without this'''
        pass

    def register(self, thread):
        '''register a Thread'''
        queue = Queue()
        self.queues[thread.name] = queue
        return queue

    def clean(self, thread):
        '''delete a Thread'''
        del self.queues[thread.name]


printer = Printer()
sys.stdout = printer


class Steamer:
    def __init__(self, target, args):
        self.thread = Thread(target=target, args=args)
        self.queue = printer.register(self.thread)

    def start(self):
        self.thread.start()
        print('This should be stdout')
        while self.thread.is_alive():
            try:
                item = self.queue.get_nowait()
                yield f'{item}<br>'
            except Empty:
                pass
        yield 'End'
        printer.clean(self.thread)


def job(times):
    for i in range(times):
        print(f'Task #{i}')
        time.sleep(1)
    print('Done')
    time.sleep(0.5)


def stream(request):
    streamer = Steamer(job, (10,))
    return StreamingHttpResponse(streamer.start())

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