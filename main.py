import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")      # coming from Render env
ADMIN_CHANNEL_ID = os.getenv("ADMIN_CHANNEL_ID")  # also from Render env

async def handle_confession(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text

    await context.bot.send_message(
        chat_id=int(ADMIN_CHANNEL_ID),
        text=f"📩 New Confession:\n\n{user_msg}"
    )

    await update.message.reply_text(
        "🔥 Your confession has been sent anonymously!"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_confession))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
