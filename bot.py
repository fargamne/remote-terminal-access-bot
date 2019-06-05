# settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import commands

updater = Updater(token=keys['token'])
dispatcher = updater.dispatcher

# commands
def start_command(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text = 'hello')

def text_message(bot, update):
	cmd = update.message.text
	for out in commands.execute(cmd):
		bot.send_message(chat_id=update.message.chat_id, text = out)

# handlers
start_command_handler = CommandHandler('start', start_command)
text_message_handler = MessageHandler(Filters.text, text_message)

# adding handlers to dispatcher
dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)


updater.start_polling(clean = True)

updater.idle()
