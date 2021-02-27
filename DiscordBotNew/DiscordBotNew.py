import discord
import config
import GetURL
from discord.ext import tasks, commands
from GetURL import checkForYoutube

client = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Bot is connected.")
    await client.change_presence(status = discord.Status, activity= discord.Game("Type '?help' for help!"))


@client.command()
async def helpp(ctx):
    await ctx.send("Commands: getYoutubeURL")

@client.command()
async def getYoutubeURL(ctx):
    link = checkForYoutube("test")
    if link is "None":
        await ctx.send("That is not a Youtube link")
    else:
        await ctx.send(link)


client.run(config.TOKEN)



