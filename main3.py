# from keep_alive import keep_alive
import discord
import requests
import json
import random 
import datetime
import os 
from dotenv import load_dotenv
client = discord.Client()

load_dotenv()

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

def become_romantic():
    response = requests.get("https://api.quotable.io/random?tags=love")
    json_data = json.loads(response.text)
    
    quote=json_data['content']
    return quote

def greet_me():

    hour_var=datetime.datetime.now().hour 
    msg=''

    if hour_var ==0 :
        msg="Sleep tight ! Good Night"
    
    elif hour_var >1 and hour_var <12:
        msg ="Good Morning"
    
    elif hour_var >=13 and hour_var <15 :
        msg="Good Afternoon"
    
    elif hour_var >=15 and hour_var <20 :
        msg="Good Evening"
    
    else :
        msg="Dinner Time"
    
    return msg 

mydate=datetime.datetime.now()
mytime =datetime.datetime.now()
 

sad_words=["sad","failed","give up","lost","miserable","alone","lonely","giveup","lose","cried","unhappy","miserable","cry","can't","angry","depressed"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "You are smart and brave student",
  "Dont give up until your work is done!",
  "You are one of the most beatiful creature created by god ",
  "When you have a dream, youve got to grab it and never let go — Carol Burnet ",
  "Nothing is impossible. The word itself says Im possible!",
  "Success is not final, failure is not fatal: it is the courage to continue that counts."
]

Bad_words=[ "motherfucker","randi rona" ,"maderchod","behenchod","ronda","fucker","maa ki chuu","Betichod","Loduchand","lodu","boka","Boka","uski maa ka bhosdra"]
mystr="date and time"
love=["love","i love you","I Love You","ilu","ILU","i love","my love"]
lites=["bc","mc","chutiya","wtf","bdsk","fuck","sala","gandu"]
raha_nahi=["cute","gorgeous","hot","moon","cutie","damn","single","baby","babydoll","myworld"]
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    message.content=(message.content).lower()
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send("Hello Everyone !")
        await message.channel.send(greet_me())

    if message.content.startswith('$date'):
        await message.channel.send(mydate.strftime("%x"))
    
    if message.content.startswith("$time"):
        await message.channel.send(mytime.strftime("%X"))

    
    if message.content.startswith("congratulations"):
        with open('stickers/congratulations.mp4','rb') as f:
            congo = discord.File(f)
            await message.channel.send(file=congo)
        await message.channel.send("Wow ! Congratualtions Buddy :)")

    if 'birthday' in message.content :
        with open('stickers/birthday.mp4','rb') as f:
            congo = discord.File(f)
            await message.channel.send(file=congo)
        await message.channel.send("Happy Birthday :)")

    if message.content.startswith(mystr):
        await message.channel.send(mydate.strftime("%c"))
    
    if any (word in message.content for word in lites):
        with open('stickers/gali.webp','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)

        with open('stickers/spam_mat_karo.webp','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)    
    
    if any (word in message.content for word in Bad_words):
        with open('stickers/tumne_upshabd_kaha.webp','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)

        with open('stickers/padhai.mp4','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)     
    if any (word in message.content for word in sad_words):
        with open('stickers/bas_karo.webp','rb') as f:
            bas_karo_bro=discord.File(f)
            # await message.channel.send(file=bas_karo_bro)
            await message.reply(file=bas_karo_bro,mention_author=True)
        await message.channel.send(random.choice(starter_encouragements))
        await message.channel.send(random.choice(starter_encouragements))
    
    if any (word in message.content for word in love):
        with open('stickers/love1.webp','rb') as f :
            love_sticker= discord.File(f)
            await message.reply(file=love_sticker)
        await message.channel.send("I love you too")
    
    if any (word in message.content for word in raha_nahi):
        with open('stickers/love_crush.mp4','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)

        with open('stickers/crush.webp','rb') as f :
            sticker= discord.File(f)
            await message.reply(file=sticker)
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$love'):
        lines=become_romantic()
        await message.channel.send(lines)
    
token=os.getenv('PASSWORD')
client.run(token)