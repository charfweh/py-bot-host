import os
import random
import discord
import urfile
client = discord.Client()
care = 407170811787608064
@client.event
async def on_ready():
    print(
        f'{client.user} is connected'

    )
    print(discord.__version__)
gmood = ["pfft","im in a guud mooooood brooo","hahaha nice nice","this is another res","yall lovely"]
bmood = ["stfu","where my senpai attt SMH","jeez bunch of dicks in chat lel","bitch fr?"]
@client.event
async def on_message(message):
    if(message.author == client.user): return
    status= message.guild.get_member(care).status
    if(status == discord.Status("dnd") or status == discord.Status("idle") or status == discord.Status("online")):
        res  = random.choice(gmood)
        await message.channel.send(res)
    elif(status == discord.Status("offline") or status == discord.Status("invisible")):
        res = random.choice(bmood)
        await message.channel.send(res)
    if(message.content.startswith("hi")):
        await message.channel.send("Yep ive started")
client.run(urfile.bot_token)
