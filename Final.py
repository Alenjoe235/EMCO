import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Load environment variables from .env file
load_dotenv()

# Get the Telegram bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a Telegram bot. Send me a message and I'll echo it back to you.")

# Define a function to handle user messages
def echo(update: Update, context: CallbackContext):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"You said: {message}")

# Define a custom filter function to check if the message is not a command
def is_not_command(update: Update):
    message = update.message.text
    return not message.startswith('/')

def main():
    # Create the Updater and pass it the bot's token.
    updater = Updater(BOT_TOKEN, update_queue=None)

    # Get the dispatcher from the bot
    dispatcher = updater.bot.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))

    # Add message handler with custom filter
    dispatcher.add_handler(MessageHandler(is_not_command, echo))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()