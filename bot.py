from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8411439065:AAEamhufk7sjBpqk6no81BM6JC-Len5QvdM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to CyberBook Vault!\nSend your payment/transaction screenshot to get the link.")

app = ApplicationBuilder().token(TOKEN).build() 
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()

