# bot.py
import random
import os
import discord
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

fuckYouShoresy = "fuck you shoresy"

phrase = "to be fair"

arianaGrande = "ariana grande"

grandeInsult = "Ariana Grande looks like she's eight. I'm giving the preschool your plate number."

fairGifs = "https://gph.is/2VmiRqO", "https://gph.is/g/4LMBedE", "https://gph.is/g/Z8pvBzz", "https://tenor.com/view/to-be-fair-group-discussion-gif-15130262" 

insults = "I made your mom so wet, Trudeau had to deploy a 24-hour national guard unit to stack sandbags around my bed." , \
        "your life is so pathetic I get a charity tax break just by hanging around you!" , \
        "your mom just liked my Instagram post from two years ago in Puerto Vallarta. Tell her I’ll put my swim trunks on for her any time she likes." , \
        "I see the muscle shirt came today. Muscles coming tomorrow? Did ya get a tracking number? Oh, I hope he got a tracking number. That package is going to be smaller than the one you’re sportin’ now." , \
        "my dad says guys with big trucks have little dinks. And that makes sense, ‘cuz you want a real big truck and got a real little dink." , \
        "go scoop it off your mom’s floor! She gives my nipples butterfly kisses." , \
        "give yer balls a tug." , \
        "your mom tried to stick her finger in my bum, but I said I only let Jonesy’s do that." , \
        "your mom ugly cried because she left the lens cap on the camcorder last night." , \
        "Tell your mom to top up the cell phone she bought me so I can FaceTime her late night." , \
        "I made your mom cum so hard that they made a Canadian heritage minute out of it and Don McKellar played my dick." , \
        "your mom shot cum straight across the room and killed my Siamese fighting fish, threw off the pH levels in my aquarium." , \
        "I made an oopsie, can you tell your mom to pick up Jonesy’s mom on the way over to my place? I double booked them by mistake, you fuckin’ loser." , \
        "tell your mom I drained the bank account she set up for me. Top it up so I can get some fucking KFC." , \
        "your breath’s so bad it gave me an existential crisis — it made me question my whole life." , \
        "tell your mom to leave me alone, she’s been laying on my waterbed since Labour Day." , \
        "shoulda heard your mom last night, he sounded like my great aunt when I pop in for a surprise visit, like, ‘Oooh!" , \
        "your mom loves anal the way I love Haagen Daz. Let's go get some fucking ice cream" , \
        "shoulda heard your mom last night, she sounded like a window closing on a Tonkenese Cat's tail.  Sounded like Ahhhhh." , \
        "your mom sneaky gushed so hard she fucked me off the waterbed last night.  Don't tell her I was thinking about Jonesy's mom the whole time." , \
        "I woke up to your mum ripping dick-dingers off my foreskin, tell her to keep her hands off my scoops." , \
        "your mom got us banned from Canada's Wonderland." , \
        "can I have your address? I'll put a little note in the mail, remind you how useless you are.… Can I grab your email? Oh, I'll just get it from your mom." , \
        "tell your mom to trim her toenails, she carves up my thighs when she gets fuckin." , \
        "tell your mom to trim her fingernails Riley's mom is getting suspcious about my war wounds." , \
        "your mom asked me to pull her hair and then hit me up for a hundo when her extensions came out." , \
        "your mom asked me to choke her and seriously not even that could shut her up." , \
        "your mom wanted 11th hour anal and lied when I asked if the chamber was empty. It's one step forward two steps back in this relationship I'm fuckin' sick of it." , \
        "your mom says she's tense with anxiety can you talk to her for me? She's gripping my weiner way too hard.", \
        "I walked in on your mom watching porn and she tried to cover it up worse than she tried to cover up your old man" , \
        "your mom wanted to watch porn and went straight for BDSM with complete disregard for how triggering that is for anyone who's been ball gagged in their sleep by Riley's mom"




@client.event
async def on_message(message):
    message.content = message.content.lower()

    if message.author == client.user: #keeps the bot from picking up it's own words
        return

    if fuckYouShoresy in message.content:
        await message.channel.send("Fuck you" + " " + message.author.mention + ", " + random.choice(insults))
   
    if arianaGrande in message.content:
        await message.channel.send(grandeInsult)

    elif phrase in message.content:
        await message.channel.send(random.choice(fairGifs))



client.run(token)
