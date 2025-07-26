import discord
from discord.ext import commands

TOKEN = "MTM5ODM5NzYzOTYyNzY0MDk0NA.G3GbKZ.mM2HCa9PCliQhB23oDJqHVRhw76rCqHVaHanN8"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} is online!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓")

bot.run(TOKEN)
