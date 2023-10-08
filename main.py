import discord
from settings import settings
from botlogic import *
from discord.ext import commands

# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot {bot.user}!')
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
        
bot.run(settings["TOKEN"])
