# this tells file is written in python
#!/usr/bin/env python

# if above line is absent, then put the UTF-8 encoding declaration on top!
# -*- coding: utf-8 -*-

# imports telegram library
import telegram 

# to initialize Updater from TOKEN
from telegram.ext import Updater

# to report errors
import logging

# Function calls
from telegram.ext import CommandHandler

# message handling
from telegram.ext import MessageHandler, Filters

# enables inline mode
from telegram import InlineQueryResultArticle, InputTextMessageContent

# handles inline query
from telegram.ext import InlineQueryHandler

# allows emojis
from emoji import emojize

##############################################
# TO CHECK TOKEN:
#
# check if token indicates the right bot
#bot = telegram.Bot(token='TOKEN')
#print(bot.getMe())
###############################################

# replace TOKEN with actual token id
updater = Updater(token='TOKEN')

# allows for quicker access to the Dispatcher when introduced locally, used by Updater:
dispatcher = updater.dispatcher 

# Logs errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# called when user initiates first conversation
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Hello, I'm a bot. Let's be friends! ")

# function is called each time "/start" is used as an input in the conversation
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Start BOT:
updater.start_polling()

# a function that is called each time a user says something, the bot repeats the same thing
def echo(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text=update.message.text)

# handles the reply after a user says something
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)


# a function that is called when user inputs "/caps"
def caps(bot, update, args):
	text_caps = ' '.join(args).upper()
	bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)

# handles the caps functions as a message
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

# an inline function when user inputs e.g. "@bubblemelonbot caps"
def inline_caps(bot, update):
	query = update.inline_query.query
	if not query:
		return
	results = list()
	results.append( InlineQueryResultArticle( id=query.upper(),title='Caps', input_message_content=InputTextMessageContent( query.upper() ) )
	)
	bot.answerInlineQuery(update.inline_query.id, results)

# handles inline query, meaning it looks for the inline function
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# handles unknown/undefined/miss-typed function calls, replies with text and emojis
def unknown(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Ohhhhh, What's this? I don't understand... ")
	bot.sendMessage(emojize("yummy :cake:", use_aliases=True))

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
