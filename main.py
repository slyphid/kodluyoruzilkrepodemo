from toke import token
import discord
from discord.ext import commands
import asyncio
import time
import os


intents = discord.Intents(messages=True,guilds=True,reactions=True,members=True,presences=True)

Bot = commands.Bot(".",intents=intents,help_command=None)


@Bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx,ext):
    Bot.load_extension(f"cogs.{ext}")

@Bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx,ext):
    Bot.unload_extension(f"cogs.{ext}")


@Bot.command()
@commands.has_permissions(administrator=True)
async def rreload(ctx,ext):
    if ext=="all":
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                Bot.unload_extension(f"cogs.{filename[:-3]}") 
                Bot.load_extension(f"cogs.{filename[:-3]}")             
    else:
        Bot.unload_extension(f"cogs.{ext}")
        Bot.load_extension(f"cogs.{ext}")
    await ctx.send("Reloaded")


@Bot.command()
@commands.has_permissions(administrator=True)
async def deactivate(ctx):
    await ctx.bot.logout()

@Bot.command()
@commands.has_permissions(administrator=True)
async def activate(ctx):
    await ctx.bot.login()



for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        Bot.load_extension(f"cogs.{filename[:-3]}")


if __name__=="__main__":

    Bot.run(token)

