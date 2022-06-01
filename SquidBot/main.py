import discord
import os
import requests
import io
from keep_alive import keep_alive
import random

client = discord.Client()
TenorToken = os.getenv('KEY')
CommandKey = 'squid '

jokes = ("/home/runner/Icebears-Test-Bot/jokes/")

intents = discord.Intents.default()
intents.members = True

tanishq_jokes = ("4lyxcj.jpg" , "5ziwkl.jpg" , "5ztzne.jpg" , "5zwt68.jpg" , "smarter.png" , "5zxn7o.jpg" , "walmart_car.png" , "windows.png" , "astro.png" , "orange.png" , "Siri_lanka.png" , "slep.png" , "sold.png" , "5zz0iz.jpg" , "toilet.png" , "wifi.png" , "6004d7.jpg" , "putin.png" , "david.png" , "604ajn.jpg" , "knife.png" , "60539m.jpg" , "609wg5.jpg" , "60djj2.jpg" , "60e3he.jpg" , "60e8z7.jpg" , "60fd9c.jpg")

client = discord.Client(intents=intents)

def get_gif(searchTerm):  # PEP8: lower_case_names for functions
    response = requests.get("https://g.tenor.com/v1/search?q={}&key={}&limit=1".format(searchTerm, TenorToken))
    data = response.json()
     
    # see urls for all GIFs
    
    for result in data['results']:
        print('- result -')
        #print(result)
        
        for media in result['media']:
            print('- media -')
            print(media)
            print(media['gif'])
            print('url:', media['gif']['url'])
         
    return data['results'][0]['media'][0]['gif']['url']

#@client.command(aliases=['c'])
#async def clear(ctx, amount=2):
  #ctx.channel.purge(limit = amount)


@client.event
async def on_member_join(member):
    await member.send("Welcome!")

@client.event
async def on_ready():
    activity = discord.Game(name="squid help")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello') or message.content.startswith("gm"):
        await message.channel.send('chal nikal')

    if message.content.startswith(f"{CommandKey}sed") or message.content.startswith("sad"):
      await message.channel.send("Depression 100")
    
    if message.content.startswith(f"{CommandKey}help"):
      await message.channel.send("""
    Instructions:
    Type squid gif <Gif-name> for gifs
    Type squid joke or squid meme or squid jokes for jokes
    **Note all commands case-sensitive** """)
    
    if (message.content.lower().startswith(f"{CommandKey}gif")):
        gif_url = get_gif(message.content.lower()[5:]) 
        response = requests.get(gif_url) 
        
        file_like_object = io.BytesIO(response.content)

        #file_name = 'image.gif'
        file_name = gif_url.split('/')[-1]
        
        await message.channel.send(file=discord.File(file_like_object, filename=file_name))  

    if message.content.lower().startswith(f"{CommandKey}meme") or message.content.lower().startswith(f"{CommandKey}jokes") or message.content.lower().startswith(f"{CommandKey}joke"):
      await message.channel.send(file=discord.File(jokes + (random.choice(tanishq_jokes))))

    if "icebear" in message.content.lower() or "siddhartha" in message.content.lower() or "bear" in message.content.lower() or "sid" in message.content.lower():
      if "side" in message.content.lower():
        pass
      else:
        await message.channel.send(file=discord.File("GrandImaginativeHeterodontosaurus-size_restricted.gif"))
      
keep_alive()
client.run(os.getenv('TOKEN'))