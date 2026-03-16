import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8718264717:AAhOpITiSR4IfuqAUVnHddAvb471nQqEmwg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Abhishek", "Kushwaha"],
        ["Yadav", "Smart"],
        ["Lalu"]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Select a name:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    print("Bot starting...")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()
