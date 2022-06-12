import discord # its a discord bot
import os
from PIL import Image
import requests
import io

from keep_alive import keep_alive
from img_scrapper import eikona_ora

client = discord.Client()

# Bot is online
@client.event
async def on_ready():
  print('News system online.\n All systems nominal. \n I am : {0.user}'
        .format(client))

# URL oras
url_ora = 'https://www.gazzetta.gr/protoselida/athlitikes-efimerides/ora-ton-sport'

  
#### Hears for msg
@client.event
async def on_message(message):
  if message.author == client.user: 
    # not from the bot itself tho...
    return

  # answers
  if message.content.startswith('eni!geia'):
    await message.channel.send('Τι θες κατώτερε οργανισμέ;')

  if message.content.startswith('eni!tipota'):
    await message.channel.send('Α, είπα μήπως.')

  if message.content.startswith('eni!ora'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_ora(url_ora)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'ora.png'))

###### On Switch
keep_alive()
my_secret = os.environ['token']
client.run(my_secret)