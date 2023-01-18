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
    
# @bot.command()
# async def makefile(ctx):
#    await file = open("testwrfile.txt", "w")
#    await file.write("This is a silly test!")
#    await file.close()


bot.run(os.environ["DISCORD_TOKEN"])
