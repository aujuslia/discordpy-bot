# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)


# @bot.event
# async def on_ready():
#    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def fuckdavid(ctx):
    channel = bot.get_channel(1052533505051070495)
    david = bot.get_user(322127489721827328)
    await channel.send(f"fuck you {david.mention}")


bot.run(os.environ["DISCORD_TOKEN"])
