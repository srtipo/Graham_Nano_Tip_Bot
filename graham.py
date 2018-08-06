## GRAHAM v4.0 Main discord bot file
GRAHAM_VERSION="4.0.0a"

import discord
from discord.ext import commands
from discord.ext.commands import Bot

import settings

from graham.models.user_model import User

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

@client.event
async def on_message(message):
	# disregard messages sent by our own bot
	if message.author.id == client.user.id:
		return

    # TODO - spam check utility that uses redis
#	if db.last_msg_check(message.author.id, message.content, is_private(message.channel)) == False:
#		return
	await client.process_commands(message)

@client.command()
async def balance(ctx):
    # IN graham v4.0 I want ALL RPC to be done in the backend, and we can wait for the result
    pass

@client.command()
async def register(ctx):
    if User.exists(ctx.message.author.id):
        # Send DM user is already registered
        pass
    else:
        user = User.create(ctx.message.author.id)
        # Send DM saying they've been created
        # We still need to get an account from the backend*
        pass

# Start the bot
client.run(settings.discord_bot_token)