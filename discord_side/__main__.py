import discord
from discord.ext import commands
import os
import asyncio
import logging
import sys
from dotenv import load_dotenv
import json
from pathlib import Path




# This is a comment! :D
load_dotenv()

## Setting up logging for doing "print" statements, except better
#logging.basicConfig(level=logging.DEBUG)
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# This is a secondary, better comment.
lru_logger = logging.getLogger('lru-dict')

#This is a comment (2.0)
## Application Interface keys so we can access Microsoft Teams and Discord respecitvley 
MC_TOKEN = os.getenv('MC_API_KEY')
DC_TOKEN = os.getenv('DC_API_KEY')


## Intents are like saying to discord "Hey, this is what we intend to do/use. Can we get permission?"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

## Creating an instance of the bot with our intents and command prefix
bot = commands.Bot(command_prefix='!', intents=intents)
bot.embed = discord.Embed() ## Attatching a embed object to the bot instance (embed means fancy display)

# Our cogs will go here, which are just our commands essentially E.X. 'cogs.Command'
extensions = []
# Test response command to ensure bot is working
@bot.command()
async def response(ctx):
    await ctx.send("Hello! This is a response from the bot!")
async def embed_test(ctx):
    channel = bot.get_channel(1444478949420830952)
    embed_dict = json.load(open(Path(__file__).parent / 'teamsMessage.json'))
    logging.info(f'Loaded embed dict: {embed_dict}')
    embed = discord.Embed.from_dict(embed_dict)

    await channel.send(embed=embed)

## This bot event is triggered whenever our bot establishes a connection with discords servers,
## it does so by establishing a "web socket" which is a live continous connection.
@bot.event
async def on_ready():
    logging.info(f'Logged in as {bot.user}')
    asyncio.create_task(embed_test(None))
    
@bot.event
async def on_error(event, *args, **kwargs):
    logging.error(f'Error in {event} {args} {kwargs}', sys.stderr)


@bot.event
async def on_load():
    logging.info("Bot is ready")    


## The very first event that is triggered when running our code. Anything you want to run
## before the bot starts should go here. This happens before on_ready() is triggered.
@bot.event
async def setup_hook():
    logging.info("Bot is starting up...")    



### If later wanted to handle events when a new user joins the server
# @bot.event
# async def on_guild_join(guild):
#     logging.info(f'Joined {guild.name}')
    



async def load_extensions(ctx=None):
    embed = bot.embed

    if ctx is None:
         for extension in extensions:
            try:
                await bot.load_extension(extension)
                return
            except Exception as e:
                logging.error(f'Failed to load extension {extension}. {e}', sys.stderr)
            return
    else:    
        for extension in extensions:
            try:
                await bot.load_extension(extension)
                
                embed.description = f'Loaded extension {extension}'
                embed.color = discord.Colour.green()
                await ctx.send(embed=embed)
            except Exception as e:
                logging.error(f'Failed to load extension {extension}. {e}', sys.stderr)
                embed.description = f'Failed to load extension {extension}. {e}'
                embed.color = discord.Colour.red()
                await ctx.send(embed=embed)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(DC_TOKEN)

    
## Need our load and unload commands here and not as cogs so we can always use them no matter what.
## This is so we can reload commands upon editing them.
@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx):
    await load_extensions(ctx)
    
    
@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx):
    for extension in extensions:
        await bot.unload_extension(extension)

    embed = bot.embed
    embed.description = "Extensions unloaded"
    await ctx.send(embed=embed)

if __name__ == '__main__':
    asyncio.run(main())