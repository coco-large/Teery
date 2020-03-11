import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from datetime import datetime, timedelta
import pytz
from discord.utils import get
from discord import Embed, Emoji, channel
from discord.ext.commands import Bot
import random

############## Basic global settings ###########################

# Defines the command prefix #
bot = commands.Bot(command_prefix='!', case_insensitive=True)

# Time Zone Variables #
st = datetime.now(pytz.utc)
bst = st + timedelta(hours=1)
cet = st + timedelta(hours=1)
eet = st + timedelta(hours=2)
msk = st + timedelta(hours=3)
aest = st + timedelta(hours=10)
pdt = st - timedelta(hours=7)

# Converts all input into lower case #
@bot.event
async def on_message(message):
    message.content = message.content.lower()
    await bot.process_commands(message)
    if redditmode == True:
        await message.add_reaction(emoji=':updoot:671329105488248843')
        await message.add_reaction(emoji=':downdoot:671329106104680448')

# Disables the defualt help command #
bot.remove_command('help')


############ Commands ###########################################

## Simple Ping command ##
@bot.command()
async def ping(ctx):
    await ctx.send('pong')


## Random Number Generator, 1-999 ##
@bot.command(pass_context = True)
async def random(ctx):
  import random
  fnum = random.randint(1, 999)
  await ctx.send(fnum)


## Returns a Cookie emoji and mentions user  ##
@bot.command(pass_context = True)
async def cookie(ctx):
  await ctx.send(ctx.message.author.mention + " Have a cookie! :cookie:")


## Code Cat. Status - BUSY FUCK OFF ##
@bot.command(pass_context = True)
async def meow(ctx):
  await ctx.send(ctx.message.author.mention + " Code cat is busy, FUCK OFF", file=discord.File("~/teery/images/ccat.gif"))



## Timezone command ##
@bot.command(pass_context = True)
async def time(ctx, *, message):
  st = datetime.now(pytz.utc)

  # Server Time #
  if message == "st" or message == "server":
    await ctx.send(st.strftime("%H:%M"))
    return

  # Central European Time #
  elif message == "cet":
    zone = st + timedelta(hours=1)
    await ctx.send(zone.strftime("%H:%M"))
    return

  # Eastern European Time #
  elif message == "eet":
    zone = st + timedelta(hours=2)
    await ctx.send(zone.strftime("%H:%M"))
    return

  # Moscow Time #
  elif message == "msk" or message == "moscow":
    zone = st + timedelta(hours=3)
    await ctx.send(zone.strftime("%H:%M"))
    return

  # Pacific Daylight Time #
  elif message == "pdt":
    zone = st - timedelta(hours=7)
    await ctx.send(zone.strftime("%A, %H:%M"))
    return

  # Australian Eastern Standard Time #
  elif message == "aest" or message == "jeral" or message == "down under":
    zone = st + timedelta(hours=10)
    await ctx.send(zone.strftime("%A, %H:%M"))
    return

  # Embeded display of all timezones #
  elif message == "list":  ## embeds all available timezones and displays to user
    emb = discord.Embed(title="**Regional Times**", description="Current times across relevant regions.")
    emb.add_field(name="Server Time **(ST)**", value=st.strftime("%H:%M"), inline=False)
    emb.add_field(name="Britiain **(GMT)**", value=st.strftime("%H:%M"), inline=False)
    emb.add_field(name="Central Europe **(CET)**", value=cet.strftime("%H:%M"), inline=False)
    emb.add_field(name="Eastern Europe **(EET)**", value=eet.strftime("%H:%M"), inline=False)
    emb.add_field(name="Moscow **(MSK)**", value=msk.strftime("%H:%M"), inline=False)
    emb.add_field(name="America, West Coast **(PDT)**", value=pdt.strftime("%A, %H:%M"), inline=False)
    emb.add_field(name="Australia East **(AEST)**", value=aest.strftime("%A, %H:%M"), inline=False)
    await ctx.send(embed=emb)

  # Vodka Time #
  elif message == "lover" or message == "Lover":
    await ctx.send("**время водки**", file=discord.File("~/teery/images/VodkaTime.png"))
    return

  # Invalid input #
  else:
    await ctx.send("Invalid or unsupported timezone")
    return

## Carol from Countdown ##
@bot.command(pass_context = True)
async def carol(ctx, game, message):

  # Numbers Game #
  import random
  if game == "numbers":
    usr_large = int(message)
    large = [25, 50, 75, 100]
    small = list(range(1, 11)) * 2
    target = random.randint(100, 999)
    try:
      tiles = random.sample(large, usr_large) + \ 
      random.sample(small, 6 - usr_large)
      emb = discord.Embed(title=str(tiles), description="**Target:** " + str(target))
      await ctx.send(embed=emb)
    except ValueError:
      await ctx.send("**Invalid input**: Please input an integer between 0 and 4. eg. ```!carol numbers <0-4>```")

  # Letters Game #
  if game == "letters":
    usr_vowels = int(message)
    consonants = [':regional_indicator_b:', ':regional_indicator_c:', ':regional_indicator_d:', ':regional_indicator_f:', ':regional_indicator_g:', ':regional_indicator_h:', ':regional_indicator_j:', ':regional_indicator_k:', ':regional_indicator_l:', ':regional_indicator_m:', ':regional_indicator_n:', ':regional_indicator_p:', ':regional_indicator_q:', ':regional_indicator_r:', ':regional_indicator_s:', ':regional_indicator_t:', ':regional_indicator_v:', ':regional_indicator_w:', ':regional_indicator_x:', ':regional_indicator_y:', ':regional_indicator_z:']
    vowels = [':regional_indicator_a:', ':regional_indicator_e:', ':regional_indicator_i:', ':regional_indicator_o:', ':regional_indicator_u:']
    try:
      if usr_vowels < 3 or usr_vowels > 5:
        await ctx.send("You must have between 3 and 5 vowels")
        return
      tiles = random.sample(vowels, usr_vowels) + \
      random.sample(consonants, 9 - usr_vowels)
      random.shuffle(tiles)
      emb = discord.Embed(title='[%s]' % ', '.join(map(str, tiles)), description="")
      await ctx.send(embed=emb)
    except ValueError:
      await ctx.send("**Invalid input**: Please input an integer between 0 and 4. eg. ```!carol letters <3-5>```")

  # help command - currently broken because the command has to take 3 vars as input ie. !carol var1 var2. Need to figure out how to be able to take either one or two vars for the command. #
  if game == "help":
    message = ""
    emb = discord.Embed(title="Countdown with Carol", description="A simple chat game emulationg the popular gameshow, Countdown.")
    emb.add_field(name="!carol rules <game>", value="Displays the rules for the requested game. There are currently two games, letters and numbers.", inline=False)
    emb.add_field(name="!carol letters <vowels>", value="Starts the letters game with the chosen amount of vowels. You must choose between 3 and 5 vowels.", inline=False)
    emb.add_field(name="!carol numbers <large_numbers>", value="Starts the numbers game with the chosen amount of large numbers. You can choose between 0 to 4 large numbers.", inline=False)

  # rules command #
  if game == "rules":
    if message == "letters":
      emb = discord.Embed(title="Countdown letters game rules", description="The contestants then have 30 seconds to form the longest single word they can, using the nine revealed letters; no letter may be used more often than it appears in the selection.")
      await ctx.send(embed=emb)
    if message == "numbers":
      emb = discord.Embed(title="Countdown numbers game rules", description="The contestant decides how many large numbers are to be used, from none to all four, after which the six tiles are randomly drawn and placed on the board. A random three-digit target number is then generated by an electronic machine, known as 'CECIL' (which stands for Countdown's Electronic Calculator In Limsa).The contestants have to work out a sequence of calculations with the numbers whose final result is as close to the target number as possible. They may use only the four basic operations of addition, subtraction, multiplication and division, and do not have to use all six numbers. A number may not be used more times than it appears on the board. Fractions are not allowed, and only positive integers may be obtained as a result at any stage of the calculation.")
      await ctx.send(embed=emb)

# Reddit Cringe command #
redditmode = False
@bot.command()
async def reddit(ctx, status):
    global redditmode
    if status == "on":
        redditmode = True
    elif status == "off":
        redditmode = False


#Help command#
@bot.command(pass_context = True)
async def help(ctx):
  emb = discord.Embed(title="Teery Commands", description="A list of basic commands for Teery")
  emb.add_field(name="!ping", value="quick bot response test", inline=False)
  emb.add_field(name="!cookie", value="Teery will give you a cookie (while stocks last)", inline=False)
  emb.add_field(name="!random", value="Generates a random number between 0 and 999", inline=False)
  emb.add_field(name="!time", value="Returns the current time of requested timezone. Usage: !time <timezone>", inline=False)
  emb.add_field(name="!time list", value="Lists all supported timezones", inline=False)
  emb.add_field(name="!carol rules <game>", value="Displays the rules for the Countdown games. there is currently a letters and numbers game.", inline=False)
  emb.add_field(name="!carol letters <vowels>", value="Starts the letters game with the chosen amount of vowels. The vowels input must be an integer, eg. '1', not 'one'.", inline=False)
  emb.add_field(name="!carol numbers <large_numbers", value="Starts the numbers game with the chosen amount of large numbers. The numbers input must be an integer, eg. '1', not 'one'.", inline=False)
  await ctx.send(embed=emb)

################# Role Assignment ####################

## Initial Message - sends a message on boot to channel() and adds reactions ##
@bot.event
async def on_ready():
    channel = bot.get_channel(586184185853640714)

    # embed code #
    emb = discord.Embed(title="**Role Selection**", description="React to this message to assign yourself a role/s. You can add and remove roles at any time by adding and removing reactions accordingly.", color=0x00ff00)
    emb.add_field(name="**Melee DPS** ", value="<:rmelee:590256130769420328>", inline=True)
    emb.add_field(name="**Ranged DPS** ", value="<:rranged:590256130870214717>", inline=True)
    emb.add_field(name="**Caster** ", value="<:rcaster:590256229134237740>", inline=True)
    emb.add_field(name="**Healer** ", value="<:rheal:590256130698248192>", inline=True)
    emb.add_field(name="**Tank** ", value="<:rtank:590256130656043028>", inline=True)
    emb.add_field(name="**Blue Mage**", value="<:blu:665171828955676682>", inline=True)
    emb.add_field(name="**Map Squad**", value="<:TakeshiLook:663489130210000907>", inline=True)
    emb.add_field(name="**Pokemon** ", value="<:slowpoge:665162491860484097>", inline=True)
    emb.add_field(name="**Monster Hunter**", value="<:mh_cheers:665162493332684810>", inline=True)
    msg = await channel.send(embed=emb) # Posts the embedded message to the #role-assign channel

    # reaction code - adds reactions to the embedded message #
    await msg.add_reaction(emoji=':rmelee:590256130769420328') #melee
    await msg.add_reaction(emoji=':rranged:590256130870214717') #ranged
    await msg.add_reaction(emoji=':rcaster:590256229134237740') #caster
    await msg.add_reaction(emoji=':rheal:590256130698248192') #healer
    await msg.add_reaction(emoji=':rtank:590256130656043028') #tank
    await msg.add_reaction(emoji=':blu:665171828955676682') #blue mage
    await msg.add_reaction(emoji=':TakeshiLook:663489130210000907') #Maps
    await msg.add_reaction(emoji=':slowpoge:665162491860484097') #pokemon
    await msg.add_reaction(emoji=':mh_cheers:665162493332684810') #monster hunter


## Role Add - Looks for reactions in channel() and adds role accordingly ##
@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel(586184185853640714)
    emoji = reaction.emoji

    if isinstance(emoji, Emoji):
        if reaction.message.channel != channel:
            return

        # Melee DPS #
        if emoji.name == 'rmelee':
            Role = discord.utils.get(user.guild.roles, name="Melee DPS")
            await user.add_roles(Role)

        # Ranged DPS #
        if emoji.name == 'rranged':
            Role = discord.utils.get(user.guild.roles, name="Ranged DPS")
            await user.add_roles(Role)

        # Caster #
        if emoji.name == 'rcaster':
            Role = discord.utils.get(user.guild.roles, name="Caster")
            await user.add_roles(Role)

        # Healer #
        if emoji.name == 'rheal':
            Role = discord.utils.get(user.guild.roles, name="Healer")
            await user.add_roles(Role)

        # Tank #
        if emoji.name == 'rtank':
            Role = discord.utils.get(user.guild.roles, name="Tank")
            await user.add_roles(Role)

        # Pokemon #
        if emoji.name == 'slowpoge':
            Role = discord.utils.get(user.guild.roles, name="Pokemon Boomers")
            await user.add_roles(Role)

        # Monster Hunter #
        if emoji.name == 'mh_cheers':
          Role = discord.utils.get(user.guild.roles, name='Cart Squad')
          await user.add_roles(Role)

        # Blue Mage #
        if emoji.name =='blu':
          Role = discord.utils.get(user.guild.roles, name='Real Content Squad')
          await user.add_roles(Role)

        # Maps #
        if emoji.name =='TakeshiLook':
          Role = discord.utils.get(user.guild.roles, name='Deep Canal Raider')
          await user.add_roles(Role)


## Role Remove - Looks for removal of reaction in channel() and removes role accordingly ##
@bot.event
async def on_reaction_remove(reaction, user):
    channel = bot.get_channel(586184185853640714)
    emoji = reaction.emoji

    if isinstance(emoji, Emoji):
        if reaction.message.channel != channel:
            return

        # Melee DPS #
        if emoji.name == 'rmelee':
            Role = discord.utils.get(user.guild.roles, name="Melee DPS")
            await user.remove_roles(Role)

        # Ranged DPS #
        if emoji.name == 'rranged':
            Role = discord.utils.get(user.guild.roles, name="Ranged DPS")
            await user.remove_roles(Role)

        # Caster #
        if emoji.name == 'rcaster':
            Role = discord.utils.get(user.guild.roles, name="Caster")
            await user.remove_roles(Role)

        # Healer #
        if emoji.name == 'rheal':
            Role = discord.utils.get(user.guild.roles, name="Healer")
            await user.remove_roles(Role)

        # Tank #
        if emoji.name == 'rtank':
            Role = discord.utils.get(user.guild.roles, name="Tank")
            await user.remove_roles(Role)

        # Pokemon #
        if emoji.name == 'slowpoge':
            Role = discord.utils.get(user.guild.roles, name="Pokemon Boomers")
            await user.remove_roles(Role)

        # Monster Hunter #
        if emoji.name == 'mh_cheers':
          Role = discord.utils.get(user.guild.roles, name='Cart Squad')
          await user.remove_roles(Role)

        # Blue Mage #
        if emoji.name =='blu':
          Role = discord.utils.get(user.guild.roles, name='Real Content Squad')
          await user.remove_roles(Role)

        # Maps #
        if emoji.name =='TakeshiLook':
          Role = discord.utils.get(user.guild.roles, name='Deep Canal Raider')
          await user.remove_roles(Role)

bot.run('NDk2NjMwNzYxNzc3MDA0NTU0.XhYNOQ.lFkXeHylgzzCCJkNgpFqA3mrMQ4')
