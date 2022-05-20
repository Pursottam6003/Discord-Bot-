# from keep_alive import keep_alive
import discord
import requests
import json
import random 
import datetime

client = discord.Client()

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

Bad_words=["bc","mc","fuck","motherfucker","Bc","Mc","Chutiya","wtf","randi rona","bdsk","maderchod","behenchod","ronda","kela","FUCK","fucker","MC","BC","maa ki chuu","Betichod","sala","Gandu","gandu","Loduchand","lodu","boka","Boka","uski maa ka bhosdra"]

mystr="date and time"
love=["love","I love you","I Love You","ilu","ILU","i love","my love","mine","My Love"]

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
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
        await message.channel.send("Wow ! Congratualtions Buddy :)")

    if message.content.startswith(mystr):
        await message.channel.send(mydate.strftime("%c"))
    if any (word in message.content for word in Bad_words):
        await message.channel.send("Shut Up! please mind your words ! Next time you will be removed!")
    
    if any (word in message.content for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))
    
    if any (word in message.content for word in love):
        await message.channel.send("I love you too")
    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$love'):
        lines=become_romantic()
        await message.channel.send(lines)
    # keep_alive()
client.run("OTQ2Mzk2NzczODY4NTAzMTAw.YheGrg.ikGG1BVW0lXf-aR-r1GU7kL3jlo")