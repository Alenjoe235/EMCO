import logging
import os
import dotenv
import streamlit as st
import pathlib
import textwrap
import google.generativeai as genai
from telegram.ext import Updater, CommandHandler, MessageHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env
dotenv.load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Define a function to handle the /start command
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

# Define a function to handle messages
def echo(update, context):
    """Echo the user message."""
    question = update.message.text
    response = get_gemini_response(question)
    update.message.reply_text(response)

# Function to get response from Google Generative AI
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Create the Updater and pass it your bot's token
updater = Updater("6890524405:AAENCT_18v9a6H7J4gid5V6o2KFyAv0Pgjw", None)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# on different commands - answer in Telegram
dp.add_handler(CommandHandler("start", start))

# on non-command i.e message - echo the message on Telegram
dp.add_handler(MessageHandler("Here", echo))

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()