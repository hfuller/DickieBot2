#!/usr/bin/env python3
#DickieBot: The Impressionable Discord Bot

import os
import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


client.run(TOKEN)