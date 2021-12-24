import discord, os, time
from discord.ext import commands

bot = commands.Bot(command_prefix = "SelfBotPrefix", self_bot=True)

@bot.event
async def on_ready():
    print("Auto Bumper Is Online!")




@bot.command()
async def start(ctx):
    while True:
        await ctx.send("!d bump")
        time.sleep(7200)

@bot.command()
async def info(ctx):
        await ctx.send("AutoBumperSelfbot|Source code at https://github.com/FlyingndCoding/AutoBumpSelfBot/ )

bot.run("TOKEN_HERE", bot = False)
