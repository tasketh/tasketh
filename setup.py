import discord
import pickle


def getServerConfigs():
  """returns the dictionary that contains server configuration"""
  with open("serverConfig.dat", "rb") as file:
    return pickle.load(file)


def updateServerConfigs(server):
  """Updates the server configuration"""
  serverConfigs = getServerConfigs()
  serverConfigs[server.id] = server
  with open("serverConfig.dat", "wb") as file:
    return pickle.dump(serverConfigs, file)


async def setPrefix(message, server):
  """Changes prefix of tasketh in a particular server
  Syntax: <current prefix>prefix <oldprefix>"""
  value = message.content.split()[-1]
  if 3>len(value)>=1:
    server.prefix = value
    updateServerConfigs(server)
    prefixEmbed = discord.Embed(title=f"Prefix changed to {server.prefix}")
    await message.channel.send(embed=prefixEmbed)
  else:
    prefixEmbed = discord.Embed(title="Error", description="Prefix cannot be longer than 3 characters")
    await message.channel.send(embed=prefixEmbed)
  

async def setTasksChannel(message, server):
  """Sets the channel to send tasks in"""
  server.taskschannel = message.channel.id
  updateServerConfigs(server)
  alert = discord.Embed(title="Task channel configured", description=f"Task channel set to <#{message.channel.id}>")
  await message.channel.send(embed=alert)
  

async def setReportsChannel(message, server):
  """Sets the channel to send reports in"""
  server.reportschannel = message.channel.id
  updateServerConfigs(server)
  alert = discord.Embed(title="Report channel configured", description=f"Report channel set to <#{message.channel.id}>")
  await message.channel.send(embed=alert)


async def setBuffer(message, server):
  """Sets the number of buffer reactions taken into account"""
  try:
    value = int(message.content.split()[-1])
    if value>=0:
      server.bufferUsers = value
      updateServerConfigs(server)
      alert = discord.Embed(title="Number of buffer users configured", description=f"Number of buffer users is now set to {value}")
      await message.channel.send(embed=alert)

    else:
      alert = discord.Embed(title="Error", description="Number of buffer users has to be a non-negative integer")
      await message.channel.send(embed=alert)

  except NameError:
    alert = discord.Embed(title="Error", description="Invalid input")
    await message.channel.send(embed=alert)
  

async def setMentionRole(message, server):
  """Changes the role thats mentioned in task embeds
  Syntax: <prefix>taskrole <role>
  Default role mentioned is everyone."""
  value = message.content.split()[-1] #this wont work if role has spaces
  server.taskMention = value
  updateServerConfigs(server)
  alert = discord.Embed(title="Mention role configured", description=f"Mention role set to <@{value}>")
  await message.channel.send(embed=alert)

