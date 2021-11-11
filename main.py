import os
import telebot
import logging
from config import *
from flask import Flask, request
import time
from apscheduler.schedulers.background import BackgroundScheduler





# def test():
#     bot.send_message(449497206, 'нижний')
# job = sched.add_interval_job(test, seconds=90)





bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)

# @bot.message_handler(commands=["start"])
# def start(message):
#     username = message.from_user.username
#     chatid = message.from_user.chatid
#     bot.reply_to(message, f"Hell {username}")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text+str(message.chat.id))

@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


def sensor():
    bot.send_message(449497206, 'верхний')

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=10)
sched.start()


if __name__ == "__main__":
    x=3
    while True:
        if x==5:
            bot.send_message(449497206, 'по времени1')
        time.sleep(2)
        bot.remove_webhook()v
        bot.send_message(449497206, 'по времени2')
        time.sleep(2)
        bot.set_webhook(url=APP_URL)
        bot.send_message(449497206, 'по времени3')
        time.sleep(2)
        server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
        bot.send_message(449497206, 'по времени4')
        time.sleep(2)
