import telegram_send
def sendMessage(body):
    telegram_send.send(conf="telegramConf",messages=[body])
