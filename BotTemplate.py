# hi :)
### Importing Libraries
import discord
import discord.ext
from discord.ext import commands

### Changable Settings

prefix = '!' ### The bot's prefix ex: "!help"
BotStatus = 'Change me in the code!' ### The bot's status whatever it is playing.

### DO NOT SHARE ###

BOTTOKEN = '' ### Need help on the token? Go to Discord Developer Portal > Applications > New Application > Bot > Build-A-Bot > & Copy the token!

### Things that the bot needs.
client = discord.Client()
client = commands.Bot(command_prefix = prefix) #put your own prefix here

@client.event
async def on_ready():
    print("Bot is online!") ### Does whatever is typed when the bot is started.
    await client.change_presence(activity=discord.Game(name=BotStatus)) ### Sets the 'Playing' Status
    ### await client.change_presence(activity=discord.Streaming(name=StreamName, url=YourTwitchURL)) ### Streaming Status 
    ### await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="SongName")) ### Listening Status
    ### await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="ShowName")) ### Watching Status
    
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! My ping is {client.latency}ms') ### A simple command, Sends a message saying the bot's ping.

client.run(BOTTOKEN)
### To invite your bot, go to your Discord Developer Portal Application > OAuth2 > URL Generator > Select 'Bot' in Scopes > Permissions You Need > Then Copy The URL!