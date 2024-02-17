import discord
import os
import json

# Load bot configuration from JSON file
with open('DMtribeDiscordBot_Cfg.json', 'r') as config_file:
    bot_config = json.load(config_file)
    TOKEN = bot_config['bot_token']
    FOLDER_PATH = bot_config['folder_path']

# Load channel mapping from JSON file
with open('channel_map.json', 'r') as channel_file:
    channel_config = json.load(channel_file)
    CHANNEL_FILES_MAP = channel_config['channels']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    for channel_id, patterns in CHANNEL_FILES_MAP.items():
        channel = client.get_channel(int(channel_id))
        if channel is None:
            continue

        for file_name in os.listdir(FOLDER_PATH):
            if any(pattern in file_name for pattern in patterns):
                file_path = os.path.join(FOLDER_PATH, file_name)
                await channel.send(file=discord.File(file_path))

    await client.close()

client.run(TOKEN)
