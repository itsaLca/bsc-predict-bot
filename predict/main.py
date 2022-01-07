import os
from predict import strategies
import asyncio
import time

def fire_and_forget(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, *kwargs)

    return wrapped

class Robot():
  def __init__(self, strategy, ammount):
    SECRET_KEY = os.getenv('secret')
    ACCOUNT = os.getenv('account')
    self.strategy = strategy
    self.ammount = ammount
    if (SECRET_KEY is None and not args.dry):
      raise Exception("SECRET_KEY is not defined in .env")
    elif (ACCOUNT is None and not args.dry):
      raise Exception("ACCOUNT is not defined in .env")  
    __import__(f'predict.strategies.{strategy}', locals(), globals())

  @fire_and_forget
  def start(self):
    SECRET_KEY = os.getenv('secret')
    ACCOUNT = os.getenv('account')
    bot = getattr(strategies, self.strategy)
    bot = bot.Bot(dry=False, account=ACCOUNT, secret_key=SECRET_KEY, bet_size_eth=self.ammount, min_balance_eth=0)
    bot.run()
