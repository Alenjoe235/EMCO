import telegram.ext

# Replace with your actual Telegram bot API token
TOKEN = "<YOUR_BOT_TOKEN>"

def handle_message(update, context):
    """Responds to incoming messages."""
    text = update.message.text
    reply_text = f"You sent: {text}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

def main():
    """Starts the bot."""
    updater = telegram.ext.Updater(token=TOKEN)
    dispatcher = updater.dispatcher

    message_handler = telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_message)
    dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if _name_ == '_main_':
    main()