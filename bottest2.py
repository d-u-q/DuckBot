import random, asyncio
from discord.ext.commands import Bot
from discord import Game
import os
print (os.listdir('.'))

token = open("tokenFile.txt", 'r')
BOT_PREFIX = ("?", "!")
TOKEN = token.read()
client = Bot(command_prefix=BOT_PREFIX)

#########################################################################
#                               COMMANDS                                #
#########################################################################

# Magic 8-ball command
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond",
                aliases=['eight_ball', "eightball", '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no.',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        'Ask Cow'
    ]
    choice = random.randint(0,len(possible_responses)-1)
    await context.send(possible_responses[choice] + ". " + context.message.author.mention)

# Square number command
@client.command(name='sq',
                description='Responds with the number squared',
                brief='squares a number')
async def square(context, number):
    num_squared = (int(number) * int(number))
    await context.send(str(number) + " squared is " + str(num_squared))

# Coin flip command
@client.command(name='coinflip')
async def coin_flip(context):
    h = "Heads"
    t = "Tails"
    flip = int(random.random()*10)
    if flip<5:
        result = h
    elif flip>=5:
        result = t

    await context.send("Magic bot-coin says: " + str(result))

# Picker command
@client.command(aliases=['pick', 'choose', 'pickforme', 'decide'])
async def picker(context, *args):
    r = random.randint(0, len(args)-1)
    await context.send("I choose... " + args[r])

""" # rps command
@client.command()
async def rps(play):
    bp = random.randint(1,3)
    if bp == 1:
        play = 'rock'
    elif bp == 2:
        play = 'paper'
    elif bp == 3:
        play = 'scissors' """

# numbers to remember
@client.command()
async def deaths(game):
    if game == 'ds3':   #DARK SOULS 3
        await game.send("123 deaths")
    elif game == 'ds2': #DARK SOULS 2
        await game.send("309 deaths. But like half of those don't count.")
    elif game == 'ds1': #DARK SOULS 1
        await game.send("33 so far.")
    elif game == 'ds3sl1': #DARK SOULS 3
        await game.send("29 deaths")

#########################################################################
#                               EVENTS                                  #
#########################################################################

# confirms login in terminal
@client.event
async def on_ready():
    #await client.change_presence(game=Game(name="with meatbags"))    
    print("Logged in as " + client.user.name)

async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers: ")
        for server in client.guilds:
            print(server.name)
        await asyncio.sleep(600)

#TODO: on twitch live event

client.loop.create_task(list_servers())
client.run(TOKEN)