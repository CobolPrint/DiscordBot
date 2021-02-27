import discord
import config
from discord.ext import tasks, commands

client = discord.Client()


bot = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Bot is connected.")
    await client.change_presence(status = discord.Status.idle, activity= discord.Game("Type '?help' for help!"))



client.run(config.TOKEN)