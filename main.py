import discord
from discord.ext import commands
import requests
import os


intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
  print("we have launched as {0.user}".format(client))

@client.command(pass_context = True)
async def tester(ctx):
  await ctx.send("hello, its working pog")

@client.command(pass_context = True)
async def join(ctx):
  if (ctx.author.voice):
    channel = ctx.message.author.voice.channel
    await channel.connect()
  else:
    await ctx.send("You are not in voice channel sadge")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("Im not in the voice channel you big dumbo")

client.run(os.environ['TOKEN'])