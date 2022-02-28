import discord
from tasks import *
from setup import *


client = discord.Client()


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

  try:
    serverPrefix = cache[message.guild.id]
  except KeyError:
    server = getServerConfigs(message.guild.id)
    serverPrefix = server.prefix

  if message.content.startswith(serverPrefix):
    try: server
    except NameError: 
      server = getServerConfigs(message.guild.id)

  #checks if the message is sent by the bot
  if message.author == client.user:           
    return

  if message.content.startswith(serverPrefix+"permit"):     
    """Gives task sending permission to the mentioned role"""
    if message.author.guild_permissions.administrator:
      await permit(message, server)
    else:
      await permDenied(message)


  if message.content.startswith(serverPrefix+"task "): 
    """Task command"""
    if server.permitted in [role.id for role in message.author.roles]:

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
    else:
      await permDenied(message)

  if message.content.startswith(serverPrefix+"taskchannel"):
    """Sets the channel to send tasks in"""
    if server.permitted in [role.id for role in message.author.roles]:
      await setTasksChannel(message, server)
    else:
      await permDenied(message)

  if message.content.startswith(serverPrefix+"reportchannel"):
    """Sets the channel to send reports in"""
    if server.permitted in [role.id for role in message.author.roles]:
      await setReportsChannel(message, server)
    else:
      await permDenied(message)
    
  if message.content.startswith(serverPrefix+"taskmention"):
    """Syntax: <prefix>taskmention <role>"""
    if server.permitted in [role.id for role in message.author.roles]:
      await setMentionRole(message, server)
    else:
      await permDenied(message)

  if message.content.startswith(serverPrefix+"prefix"):
    """Syntax: <current prefix>prefix <oldprefix>"""
    if server.permitted in [role.id for role in message.author.roles]:
      await setPrefix(message, server)
    else:
      await permDenied(message)

  if message.content.startswith(serverPrefix+"bufferusers"):
    """Syntax: <current prefix>bufferusers <custom number of buffer users>"""
    if server.permitted in [role.id for role in message.author.roles]:
      await setBuffer(message, server)
    else:
      await permDenied(message)


client.run(config('BOT_TOKEN'))