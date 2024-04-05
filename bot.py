import telegram.ext

# Replace with your actual Telegram bot API token
TOKEN = "6890524405:AAENCT_18v9a6H7J4gid5V6o2KFyAv0Pgjw"

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

if __name__ == '__main__':
    main()