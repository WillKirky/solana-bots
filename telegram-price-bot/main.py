import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 Welcome to the SOL Price Bot!\n\n"
        "Use /price to get the current price of Solana SOL/USD.\n\n"
        "Quick and simple 🚀"
    )
    await update.message.reply_text(welcome_message)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data["solana"]["usd"]
        await update.message.reply_text(f"Current SOL Price: ${price:.2f} USD 💰")
    except Exception as e:
        await update.message.reply_text("⚠️ Could not fetch the price at the moment.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))

    app.run_polling()

if __name__ == "__main__":
    main()
