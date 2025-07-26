import discord
from discord.ext import commands
import os  # needed for environment variables

# ✅ Get the token from Railway's environment variables (KEY = TOKEN)
TOKEN = os.getenv("TOKEN")

# ✅ Basic bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online and connected!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

# ✅ Run the bot
bot.run(TOKEN)
