import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
from math import *
from webserver import keep_alive
import os


client = commands.Bot(command_prefix=".s ")

client.remove_command('help')

@client.event
async def on_ready():
    print("[INFO] On.")
    print(f"""
    [INFO] Bot info:
    User ID: {client.user.id}
    Name: {client.user.name}
    """)

@client.event
async def on_member_join(member):
    print(f'[INFO] {member} joined.')

@client.event
async def on_member_remove(member):
    print(f'[INFO] {member} left.')

@client.command(name="help", brief="The Snom is here to help.")
async def help(ctx, cmd=None):
    embed=discord.Embed(colour=discord.Colour(0xbfcdff), title="Help", description="Here's the list of available commands.")
    for command in ctx.bot.commands:
        embed.add_field(name=f"{command}", value=f"{command.brief}", inline=True)
    embed.set_footer(text=f"The command prefix is {client.command_prefix}")
    await ctx.send(embed=embed)

@client.command(brief="Ask the ping, and the Snom will pong! (in ms)")
async def ping(ctx):
    """
    Ask the ping, and the Snom will pong! (in ms)
    No arguments required.
    """
    print(f"[INFO][COMMAND]Ping by {ctx.message.author.name}. Actual bot latency: {client.latency * 1000} ms.")
    await ctx.send(f'The snom has Pong! ({round(client.latency * 1000,2)} ms)')

@client.command(brief="Say 'Hi' to the Snom.")
async def hi(ctx):
  """
  Say 'Hi' to the Snom.
  No arguments required.
  """
  sentences=['OwO','UwU',":3","^_^",'*Hiii!*']
  chosed_sentence=random.choice(sentences)
  print(f"[INFO][COMMAND]'hi' command by {ctx.message.author.name}. Chosen sentence: '{chosed_sentence}'")
  await ctx.send(chosed_sentence)

@client.command(name="python", brief="[DEV]The Snom will execute Python commands!")
async def remote_command(ctx, *,cmd=None):
    """
    The Snom will execute Python commands!
    Arguments:
    <cmd>: any Python command
    Being the developer is required! :)
    """
    if ctx.message.author.id == 332082083604463616:
        try:
            if cmd != None:
                await ctx.send(f"""```py
{eval(cmd)}
```""")
            if cmd is None:
                await ctx.send("The Snom can't execute nothing, please give him something to execute.")
        except:
            await ctx.send("The command you were trying to execute got an error!\nAlso, you can't use functions such as defining variables, `import` and stuff like that.")
    else:
        await ctx.send("You are not the developer! Intruder!")

@client.command(brief="Yummy waffles...")
async def waffle(ctx):
    """
    Yummy waffles...
    Call this command and the Snom will send Waffle pics.
    No arguments required.
    """
    await ctx.send("",file=discord.File(f"wafflePics/waffle{random(1,10)}.jpg"))

@client.command(name="stop", brief="[DEV]This completely stop the bot.")
async def stop_bot(ctx):
    """
    This completely stop the bot.
    No argument required but being the developer is required :)
    """
    if ctx.message.author.id == 332082083604463616:
        await ctx.send("The Snom is going to sleep.")
        await client.close()
    else:
        await ctx.send("You are not the developer! Intruder!")






keep_alive()
client.run('NjU2OTM3NTU3MDk0ODI2MDE0.Xf5D4w.V-2bH2v5h5ab4B67bHkgBuLz_Yo')
