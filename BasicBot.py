import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import time as timemod

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="UMUC Cyber Padawan Bot", command_prefix="!", pm_help = False)

#=======================================================#
#                    Startup Sequence                   #
#=======================================================#
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
    print('Created by Habchy#1665')
    return await client.change_presence(game=discord.Game(name='PYTHON BOT')) #This is buggy, let us know if it doesn't work.

#=======================================================#
#                    Commands                           #
#=======================================================#
@client.command()
async def ping(*args):
    await client.say(":ping_pong: Pong!!")
    await asyncio.sleep(3)

@client.command()
async def silly(*args):
    await client.say("Why did the HTTP request get pulled over on the interstate?\nIt was going over 80!")
    await asyncio.sleep(3)

@client.command()
async def tutorial(*args):
    await client.say("https://github.com/ajackal/python_tutorials/wiki")
    await asyncio.sleep(3)

@client.command()
async def new(*args):
    await client.say("You can write a new bot function like this!```python\n" + """
@client.command()
async def COMMANDNAME(*args):
    await client.say("SAYTHIS")
    await asyncio.sleep(3)```""")
    await asyncio.sleep(3)
    
@client.command()
async def time(*args):
    await client.say(str(timemod.localtime().tm_hour).zfill(2)+str(timemod.localtime().tm_min).zfill(2))
    await asyncio.sleep(3)
    
@client.command()
async def test(*args):
    await client.say("who goes there?")
    await asyncio.sleep(3)

@client.command()
async def python(*args):
    await client.say("Does this answer your question?")
    await client.say("https://python101.pythonlibrary.org/intro.html")
    await asyncio.sleep(3)

@client.command()
async def echo(*args):
    await client.say("You said:")
    for word in args:
        await client.say(word)
    
    await asyncio.sleep(3)


@client.command(pass_context=True)
async def create_private_channel(ctx, channel_name, *users : discord.User):
    
    '''Create a private channel named name, and then add users.'''

    #Initialize server as the server in which this command is being run from
    server = ctx.message.server
    #Ensure the channel has at least one user
    if not users:
        await client.say("Usage:  create_private_channel <name> <users...>")

    #Deny everyone read_messages permissions
    #Grant Group read_messages permissions
    everyone_perms = discord.PermissionOverwrite(read_messages=False)
    group_perms = discord.PermissionOverwrite(read_messages=True)

    #overwrite the channel default with deny everyone rule
    everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)

    #Make a group that includes the listed users and the bot- add this to the overwrite
    group = []
    group.append(discord.ChannelPermissions(target=server.me, overwrite=group_perms))
    for user in users:
        group.append(discord.ChannelPermissions(target=user, overwrite=group_perms))


    #create the channel as a text channel with "everyone" and "group" overwrite permissions
    await client.create_channel(server, channel_name, everyone, *group, type=discord.ChannelType.text)                                       
    await asyncio.sleep(3)



    
#@client.command()
#async def ping(*args):
#    await client.say(":ping_pong: Pong!!")
#    await asyncio.sleep(3)


#Runs the bot
#client.run('')

#Original Author Information
#
#
#
# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
