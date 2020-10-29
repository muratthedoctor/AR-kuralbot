import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
import asyncio
import time
import csv
import random
import os

client = discord.Client()
#client = commands.Bot(command_prefix = "_")

@client.event
async def on_ready():
     print("Bot is ready!")
     print('Logged in as')
     print(client.user.name)
     print('------')

@client.event
async def on_message(message):
     if message.author == client.user:
          return

     if message.content.startswith("!help"):
          await message.channel.send("```1. 'orospu' yazarsan 'eğvle eğvle' yazarım.\n2. '!random' yazarsan rastgele kural yazarım.\n3. '!hello' yazarsan 'Hello [username]' yazarım.\n5. Kural eklemek istiyorsan '!add_kural 123½ÖRNEK KURAL HEBELE.' şeklinde gir.\n6. '!kactane' yazarsan kaç kural olduğun hatırlatırım. (Yeni kural eklerken lazım.)```")

     if message.content == "orospu":
          await message.channel.send("eğvle eğvle")
          
     if message.content.startswith("!catvibe"):
          
          '''with open('catvibe.gif', 'rb') as f:
               picture = discord.File(f)
               await message.channel.send(picture)'''
          
          embed = discord.Embed(title="Title", description="Desc", color=0x00ff00) #creates embed
          file = discord.File("/catvibe.gif", filename="image.gif")
          embed.set_image(url="attachment://image.gif")
          await ctx.send(file=file, embed=embed)

     if message.content.startswith("!add_kural"):
          with open('arkurallar', 'a') as txtfile: 
               txtfile.write("\n"+message.content[11:])
          await message.channel.send("Kural başarıyla eklendi.")
     
     if message.content.startswith("!random"):
          with open('arkurallar') as csvfile:
               csv_reader = csv.reader(csvfile, delimiter='½')
               nums = []
               kurallar = []
               count = -1
               for row in csv_reader:
                    num = row[0]
                    kural = row[1]
                    nums.append(num)
                    kurallar.append(kural)
                    count += 1
               random.seed()
               rand = random.randint(1, count)
               await message.channel.send(f'Kural {nums[rand]}) {kurallar[rand]}')

     if message.content.startswith("!kactane"):
          with open('arkurallar') as csvfile:
               csv_reader = csv.reader(csvfile, delimiter='½')
               count = -1
               for row in csv_reader:
                    count += 1
          await message.channel.send(f'{count} tane kuralımız var.')

     if message.content.startswith("!hello"):
          await message.channel.send("Hello {0.author.mention}".format(message))
     
     if message.content.startswith("!yılan"):
          await message.channel.send("tısssss :snake: :snake:")
          
     if message.content.startswith("ride or die"):
          await message.channel.send("Remember?:red_car:")

"""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('token')
"""
token = os.environ.get("BOT_TOKEN")
client.run(token)
#client.run(str(os.environ.get('BOT_TOKEN')))
