import discord
import asyncio
from discord.ext import commands
import requests

F = open("./config/token.txt", "r")
P = open("./config/prefix.txt", "r")
U = open("./config/url.txt", "r")
description = '''Volumio Controller'''
bot = commands.Bot(command_prefix=commands.when_mentioned_or(P.read()), description=description)
url = U.read()


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Volumio Controller!"))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.utils.oauth_url(bot.user.id))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing Argument!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You don´t have Permission to do that!")
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("The Bot hasn't the missing Permission!")
    if isinstance(error, commands.NotOwner):
        await ctx.send("This Command is only for my Lord!")



@bot.command(aliases=['next'])
@commands.is_owner()
async def skip(ctx):
    '''
    Skips the Current Song on your Volumio
    '''
    print(ctx.author.name + " executed skip")
    m = requests.get(url + "/api/v1/commands/?cmd=next")
    await ctx.send(m.json()["response"])

@bot.command(aliases=['previous'])
@commands.is_owner()
async def prev(ctx):
    '''
    Plays the Previous Song on your Volumio
    '''
    print(ctx.author.name + " executed prev")
    m = requests.get(url + "/api/v1/commands/?cmd=prev")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def pause(ctx):
    '''
    Pause the Current Song on your Volumio
    '''
    print(ctx.author.name + " executed pause")
    m = requests.get(url + "/api/v1/commands/?cmd=pause")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def stop(ctx):
    '''
    Stop the Current Song on your Volumio
    '''
    print(ctx.author.name + " executed stop")
    m = requests.get(url + "/api/v1/commands/?cmd=stop")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def toggle(ctx):
    '''
    Toggle between play and pause
    '''
    print(ctx.author.name + " executed toggle")
    m = requests.get(url + "/api/v1/commands/?cmd=toggle")
    await ctx.send(m.json()["response"])

@bot.command(aliases=['vol'])
@commands.is_owner()
async def volume(ctx, vol):
    '''
    Set the Volume of your Volumio
    '''
    print(ctx.author.name + " executed volume")
    try:
        vol = int(vol)
        if vol > 100:
            await ctx.send("Error, please provide a valid Volume.")
            return
        if vol < 0:
            await ctx.send("Error, please provide a valid Volume.")
            return
        vol = str(vol)
        m = requests.get(url + "/api/v1/commands/?cmd=volume&volume=" + vol)
        await ctx.send(m.json()["response"])
    except:
        await ctx.send("Error, please insert a Number!")

@bot.command()
@commands.is_owner()
async def play(ctx):
    '''
    Starts playing
    '''
    print(ctx.author.name + " executed play")
    m = requests.get(url + "/api/v1/commands/?cmd=play")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def clear(ctx):
    '''
    Clear the queue
    '''
    print(ctx.author.name + " executed clear")
    m = requests.get(url + "/api/v1/commands/?cmd=clearQueue")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def playplaylist(ctx, name):
    '''
    Play a Playlist
    '''
    print(ctx.author.name + " executed playplaylist")
    m = requests.get(url + "/api/v1/commands/?cmd=playplaylist&name=" + name)
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def listplaylists(ctx):
    '''
    List Playlists
    '''
    print(ctx.author.name + " executed listplaylists")
    m = requests.get(url + "/api/v1/listplaylists")
    r = m.text
    r = r.replace("[", "")
    r = r.replace("]", "")
    r = r.replace('"', '')
    r = r.replace(',', ', ')
    await ctx.send(r)


@bot.command(aliases=['loop'])
@commands.is_owner()
async def repeat(ctx):
    '''
    Repeat a track
    '''
    print(ctx.author.name + " executed repeat")
    m = requests.get(url + "/api/v1/commands/?cmd=repeat")
    await ctx.send(m.json()["response"])

@bot.command(aliases=['shuffle'])
@commands.is_owner()
async def random(ctx):
    '''
    Random Makes the order in which tracks are played random
    '''
    print(ctx.author.name + " executed random")
    m = requests.get(url + "/api/v1/commands/?cmd=random")
    await ctx.send(m.json()["response"])

@bot.command()
@commands.is_owner()
async def ping(ctx):
    '''
    Ping
    '''
    print(ctx.author.name + " executed ping")
    m = requests.get(url + "/api/v1/ping")
    await ctx.send(m.text)

@bot.command(aliases=['info', "stats", "status", "np"])
@commands.is_owner()
async def nowplaying(ctx):
    '''
    Displays current Song!
    '''
    print(ctx.author.name + " executed nowplaying")
    m = requests.get(url + "/api/v1/getSystemInfo")
    await ctx.send("Track: " + m.json()["state"]["track"])


bot.run(F.read())
