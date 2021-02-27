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
async def getYoutubeURL(ctx, url):
    link = checkForYoutube(url)
    if link is 0:
        await ctx.send("That is not a Youtube link")
    else:
        youtubeFile = open(config.YOUTUBETXTFILE, "a")
        youtubeFile.writelines(link + "\n")
        youtubeFile.close


client.run(config.TOKEN)



