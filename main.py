import discord
import os
import keep_alive
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = ['C']) #put your own prefix here


@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def why(ctx):
  await ctx.send("I came, I saw, I conquered.  That's why.") 
@client.command()
async def revolution(ctx):
  await ctx.send("https://c.tenor.com/2YZV8C1eZNEAAAAC/party.gif")
@client.command()
async def guide(ctx):
  await ctx.send("Experience is the teacher of all things.") 
@client.command()
async def story(ctx):
  await ctx.send("Several millenials ago, there was a tree dryad named Daphne.  I forgot who shot the love arrow, being in so many battles with Pompey, but one of them did and landed it on Apollo.  Apollo then fell in love with Daphne.  The dryad didn't like him back however, so Apollo chased her everywhere she went. Eventually, she got so tired of this that she requested to become a permanent tree.  Apollo, being sad and all, decided to create a new flower after her called Daphadills(Again, I forgot how to spell the flower).")
@client.command()
async def conquer (ctx,member : discord.Member):
  await ctx.send( member.mention + " has  been conquered.")
    #simple command so that when you type "!ping" the bot will respond with "pong!"

#qs = ["Hello user", "I love cats", "Dogs are eh"]

#await ctx.send(qs[random.randint(0,len qs)])


@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+ member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")
keep_alive.keep_alive()
client.run("ODcyOTkyNTgyOTExODE1NzMx.YQx7sw.kuvoGw0FjmQqwoZx1-SqXcNV91g") #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!