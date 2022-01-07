from os import environ
import telegram_send
import imgkit
def sendMessage(body, id):
    telegram_send.send(conf="telegramConf",messages=[body])
