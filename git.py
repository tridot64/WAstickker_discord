import discord
import os

client = discord.Client()

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 = str1 + '\n' + ele  
    
    # return string  
    return str1 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content=='$bello':
    	op = open("universe.jpg","rb")
    	f = discord.File(op)
    	auth = message.author.name
    	await message.delete()
    	await message.channel.send(content=auth, tts=False, embed=None, file=f, files=None, delete_after=None, nonce=None, allowed_mentions=None, reference=None, mention_author=None)
    
    if message.content.startswith('*'):
    	m = message.content
    	st = os.listdir()
    	fst = listToString(st)
    	filename = m[1:]+".webp"
    	if filename not in fst:
    		filename = m[1:]+".gif"
    	with open(filename,"rb") as op:
	    	f = discord.File(op)
	    	auth = message.author.display_name
	    	await message.delete()
	    	await message.channel.send(content=auth, tts=False, embed=None, file=f, files=None, delete_after=None, nonce=None,allowed_mentions=None, reference=None, mention_author=None)
	    	
    if message.content == '$list':
    	st = os.listdir('/home/tridot/Documents/projects/dispal')
    	fst = listToString(st)
    	await message.channel.send(content=fst, tts=False, embed=None, file=None, files=None, delete_after=None, nonce=None,allowed_mentions=None, reference=None, mention_author=None)

client.run('your tokken here')

