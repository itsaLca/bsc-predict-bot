import telegram_send
def sendMessage(body, id):
    telegram_send.send(conf="telegramConf",messages=[body])
