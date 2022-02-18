import discord
from tasks import *
from setup import *
from server import *
from decouple import config

client = discord.Client()

serverConfigs = getServerConfigs()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(joinedGuild):
  #it will forget previous configs if bot is re-added into a server
  server = Server(joinedGuild.id)
  updateServerConfigs(server)
  
@client.event
async def on_message(message): 
  """Function called when a message is sent"""

  serverConfigs = getServerConfigs()
  server = serverConfigs[message.guild.id]

  #checks if the message is sent by the bot
  if message.author == client.user:           
    return

  #task command
  if message.content.startswith(server.prefix+"task "): #task command  

    #if task and report channel is'nt set up, then throw an error
    if None in (server.taskschannel, server.reportschannel):
      alert = discord.Embed(title="Alert",description= "Channel ID for tasks and reports haven't been configured. Please use the help command and configure them")
      await message.channel.send(embed=alert)

    else:
      #Separates the command and assigns them to the dictionary.
      commandList = message.content[len(server.prefix)+4::].strip().split(server.syntaxDelimiter)
      taskDetails = {'taskUsers':int(commandList[0]), 'taskHours':commandList[1], 'taskName':server.syntaxDelimiter.join(commandList[2::])}
    
      sentTaskMsg = await sendTaskEmbed(message, client, taskDetails, server)
      await message.add_reaction(server.reactEmoji)
      userList = await collectResponses(sentTaskMsg, client, taskDetails, server)
      await closeTask(sentTaskMsg, taskDetails, server)
      await sendReport(client, taskDetails, userList, server)


  if message.content.startswith(server.prefix+"taskchannel"):     
    """Sets the channel to send tasks in"""
    await setTasksChannel(message, server)

  if message.content.startswith(server.prefix+"reportchannel"):
    """Sets the channel to send reports in"""
    await setReportsChannel(message, server)
  
  if message.content.startswith(server.prefix+"taskrole"):
    """Syntax: <prefix>taskrole <role>"""
    await setMentionRole(message, server)

  if message.content.startswith(server.prefix+"prefix"):
    """Syntax: <current prefix>prefix <oldprefix>"""
    await setPrefix(message, server)

  if message.content.startswith(server.prefix+"bufferusers"):
    """Syntax: <current prefix>bufferusers <custom number of buffer users>"""
    await setBuffer(message, server)

client.run(config('TOKEN'))
