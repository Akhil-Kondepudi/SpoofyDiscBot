import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import os

FFMPEG_PATH = '/home/runner/DiscBot/node_modules/ffmpeg-static/ffmpeg'
discord.opus.load_opus("./libopus.so.0.8.0")

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
    voice = await channel.connect()
    source = FFmpegPCMAudio('tester.mp3')
    player = voice.play(source)
  else:
    await ctx.send("You are not in voice channel sadge")

@client.command(pass_context = True)
async def leave(ctx):
  if (ctx.voice_client):
    await ctx.guild.voice_client.disconnect()
  else:
    await ctx.send("Im not in the voice channel you big dumbo")

@client.command(pass_content = True)
async def pause(ctx):
  voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
  if voice.is_playing():
    voice.pause()
  else:
    await ctx.send("there is no audio playing right now")

@client.command(pass_content = True)
async def resume(ctx):
  voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
  if voice.is_paused():
    voice.resume()
  else:
    await ctx.send("there is no audio prepped right now baka")

@client.command(pass_content = True)
async def stop(ctx):
  voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
  voice.stop()

@client.command(pass_content = True)
async def play(ctx, arg):
  voice = ctx.guild.voice_client
  source = FFmpegPCMAudio(arg + ".mp3")
  player = voice.play(source)

client.run(os.environ['TOKEN'])