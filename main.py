import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} olarak aktif oldu!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

# BURAYA DISCORD DEVELOPER PORTALDAN ALDIĞIN TOKEN'I YAZACAKSIN
bot.run('MTQ5MDA3MTU2OTEzMTc2NTk4MQ.G72rfL.H5YZgyS_-maeatFrJyqMwCF5SLRGpZJU7Ya_3I')
