import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def chatid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await update.message.reply_markdown(f'`{chat_id}`')

if __name__ == '__main__':
    if BOT_TOKEN is None:
        raise ValueError("Please set the TELEGRAM_BOT_TOKEN environment variable.")

    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('id', chatid_command))
    app.add_handler(CommandHandler('chatid', chatid_command))
    app.run_polling()
