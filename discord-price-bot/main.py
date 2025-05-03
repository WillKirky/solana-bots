import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set command prefix
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Price fetch function
def fetch_sol_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    price = data['solana']['usd']
    return price

# On Ready Event
@bot.event
async def on_ready():
    print(f"✅ {bot.user} has connected to Discord!")

# !start Command
@bot.command(name="start")
async def start(ctx):
    message = (
        "👋 Welcome to **ToolVault PriceBot**!\n\n"
        "Use `!price` to get the live Solana (SOL) price in USD 💰.\n"
        "More alpha tools coming soon 👾"
    )
    await ctx.send(message)

# !price Command
@bot.command(name="price")
async def price(ctx):
    try:
        sol_price = fetch_sol_price()
        await ctx.send(f"💸 Current Solana (SOL) price: **${sol_price:.2f} USD**")
    except Exception as e:
        await ctx.send("⚠️ Error fetching price. Please try again later.")
        print(e)

# Run the bot
bot.run(DISCORD_BOT_TOKEN)
