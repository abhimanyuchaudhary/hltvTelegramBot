import main
import json
import telegram
from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
TOKEN = '794182965:AAFDL4PgsHzLfcbIk3mexD_k6Rp4uvUGM9M'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="chhokra gay")
def showMatches(update, context):
	result = main.get_matches()
	for i in range(5):
		date = str(result[i]['date'].decode("utf-8"))
		time = str(result[i]['time'].decode("utf-8"))
		team1 = str(result[i]['team1'].decode("utf-8"))
		team2 = str(result[i]['team2'].decode("utf-8"))
		event = str(result[i]['event'].decode("utf-8"))
		context.bot.send_message(chat_id=update.message.chat_id, text=date + time + "\n" + team1 + " v "+ team2 + "\n" +event)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
matches_handler = CommandHandler('getMatches', showMatches)
dispatcher.add_handler(matches_handler)
updater.start_polling()

# print(str(main.get_matches()))

