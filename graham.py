## GRAHAM v4.0 Main discord bot file
GRAHAM_VERSION="4.0.0a"

import discord
from discord.ext import commands
from discord.ext.commands import Bot

import settings

# Create discord client
client = Bot(command_prefix=COMMAND_PREFIX)
client.remove_command('help')

@client.event
async def on_ready():
	logger.info("Graham v%s started.", GRAHAM_VERSION)
	logger.info("Discord.py API version %s", discord.__version__)
	logger.info("Name: %s", client.user.name)
	logger.info("ID: %s", client.user.id)
	await client.change_presence(activity=discord.Game(settings.playing_status))

# Start the bot
client.run(settings.discord_bot_token)