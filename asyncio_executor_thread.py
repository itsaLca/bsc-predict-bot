import asyncio
import concurrent.futures
import logging
import sys
import time

class robotInstance:
    def __init__(self):
        self.closed = 0
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.event_loop = self.get_or_create_eventloop()
    def status(self):
        return self.event_loop.is_running()
    async def run_tasks(self, task):
        self.event_loop.run_forever(task)
        return self.event_loop.is_running()

    async def doTask(self, task):
        self.event_loop.create_task(
            self.run_tasks(task)
        )
    async def stopTask(self):
        self.closed = 1
        self.event_loop.stop()
        self.event_loop.close()

    def get_or_create_eventloop(self):
        try:
            return asyncio.get_event_loop()
        except RuntimeError as ex:
            if "There is no current event loop in thread" in str(ex):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                return asyncio.get_event_loop()