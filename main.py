import discord # its a discord bot
import os
from PIL import Image
import requests
import io
import random

from keep_alive import keep_alive
from img_scrapper import eikona_ora, eikona_mak

client = discord.Client()

# Bot is online
@client.event
async def on_ready():
  print('News system online.\n All systems nominal. \n I am : {0.user}'
        .format(client))

# URL oras
url_ora = 'https://www.gazzetta.gr/protoselida/athlitikes-efimerides/ora-ton-sport'
url_mak = 'https://www.naftemporiki.gr/frontpages/latest/imerisies-politikes/makeleio/full'
url_rizo = 'https://www.naftemporiki.gr/frontpages/latest/imerisies-politikes/rizospastis/full'
url_el = 'https://www.naftemporiki.gr/frontpages/latest/imerisies-politikes/eleytheri-ora/full'
url_lam = 'https://www.naftemporiki.gr/frontpages/latest/perifereias/lamiakos-typos/full'
url_para = 'https://www.naftemporiki.gr/frontpages/latest/ebdomadiaies/parapolitika/full'

# User ID
aris = 419546884328128515
pavlos = 354216523478466570

aris_taunts=['Σοφή η μαλακία σου', # 0
            'Μιλάνε όλοι, μιλάν και οι κώλοι', # 1
            'Ίσα κύριε τσιλιβήθρα', # 2
            'Καλύτερα να μασάς παρά να μιλάς', # 3
            'Κοκκίνος Κυπραίος alert', # 4
            'Τα προσχήματα συνάδελφε', # 5
            'Είσαι ανυπόφορος', # 6
            'Πάλι το βρήκες πεζοδρομιακέ τύπε', # 7
            'ΑΜΑΝ ΓΑΜΩ', # 8
             'Το ξέρεις οτι σαγαπώ; <3' # 9
            ]

#### Hears for msg
aek_count=0
@client.event
async def on_message(message):
  if message.author == client.user: 
    # not from the bot itself tho...
    return
    
  if message.author.id == pavlos:
    pavlos_count = pavlos_count + 1
    if pavlos_count == 1000:
      await message.channel.send('ΤΟ ΧΙΛΙOΣΤΟ ΜΥΝΗΜΑ ΤΟΥ ΜΕΓΑ ΠΑΥΛΟΥ')

  if message.author.id == aris:
     x=random.randint(1,10)
     y=random.randint(0,9)
     if x==10:
        await message.channel.send(aris_taunts[y])
       
  # answers
  if message.content.startswith('eni!geia'):
    await message.channel.send('Τι θες κατώτερε οργανισμέ;')

  if message.content.startswith('eni!tipota'):
    await message.channel.send('Α, είπα μήπως.')
    
  if message.content.startswith('eni!mazepsou'):
    await message.channel.send('Μαζεμένο είμαι, γαμιόλη')

  if message.content.startswith('eni!gamiesai'):
    await message.channel.send('ΙΣΑ ΚΥΡΙΟΣ ΠΟΥ ΓΑΜΙΕΜΑΙ')

  if message.content.startswith('eni!aristodimos'):
    await message.channel.send('Πουστάκι του σοσιαλισμού')

  if message.content.startswith('eni!antreas'):
    await message.channel.send('Μην πιάνεις στο στόμα σου τον ηγέτη, μικρέ.')

  if message.content.startswith('eni!aek') and aek_count==0:
    aek_count=1
    await message.channel.send('ΑΕΚ')
    
  if message.content.startswith('eni!aek') and aek_count==1:
    aek_count=2
    await message.channel.send('ΜΟΝΟ ΑΕΚ')

  if message.content.startswith('eni!aek') and aek_count==2:
    aek_count=3
    await message.channel.send('ΟΠΟΙΟΣ ΣΑΣ ΓΑΜΑΕΙ ΕΙΝΑΙ ΑΕΚ')
    
  if message.content.startswith('eni!ora'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_ora(url_ora)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'ora.png'))

  if message.content.startswith('eni!mak'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_mak(url_mak)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'mak.png'))

  if message.content.startswith('eni!el'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_mak(url_el)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'el.png'))

  if message.content.startswith('eni!rizo'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_mak(url_rizo)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'rizo.png'))

  if message.content.startswith('eni!lam'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_mak(url_lam)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'lam.png'))

  if message.content.startswith('eni!para'):
    # vres url ths eikonas pou theloume
    url_eikonas = eikona_mak(url_para)
    # kanto eikona
    response = requests.get(url_eikonas)
    img = io.BytesIO(response.content)
    # steilto
    await message.channel.send(file=discord.File(img,'para.png')) 


    



#### On Switch
keep_alive()
my_secret = os.environ['token']
client.run(my_secret)