import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from .env
load_dotenv()

# Read the secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
GDRIVE_LINK = os.getenv("GDRIVE_LINK")

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Payment confirmed!\nHere is your book 📚:\n" + GDRIVE_LINK
    )

# Build the bot app
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Start polling (long-running)
if __name__ == "__main__":
    app.run_polling()

