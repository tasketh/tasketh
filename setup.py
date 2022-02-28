import discord
import pickle
from discord.ext import commands

#bot = commands.Bot(command_prefix='!')

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
  
async def llama():
  pass

async def permit(message, server):
  """Changes the role that has permission to create tasks and change setting.
  Syntax: <prefix>taskmention <role>
  Default role mentioned is everyone."""
  value = message.content.split()[-1] #this wont work if role has spaces
  roles = {}
  for role in message.guild.roles:
    roles[role.name] = role.id
  try:
    server.permitted = roles[value]
    updateServerConfigs(server)
    alert = discord.Embed(title="Permission role configured", description=f"Permission role set to <@&{server.permitted}>")
    await message.channel.send(embed=alert)
  except KeyError:
    alert = discord.Embed(title="Error", description="That role doesn't exist")
    await message.channel.send(embed=alert)


async def setMentionRole(message, server):
  """Changes the role thats mentioned in task embeds
  Syntax: <prefix>taskmention <role>
  Default role mentioned is everyone."""
  value = message.content.split()[-1] #this wont work if role has spaces
  roles = {}
  for role in message.guild.roles:
    roles[role.name] = role.id
  try:
    server.taskMention = roles[value]
    updateServerConfigs(server)
    alert = discord.Embed(title="Permission role configured", description=f"Permission role set to <@&{server.taskMention}>")
    await message.channel.send(embed=alert)
  except KeyError:
    alert = discord.Embed(title="Error", description="That role doesn't exist")
    await message.channel.send(embed=alert)

async def permDenied(message):
  desc= "BECAUSE I DON'T WANT TO. PERMISSION DENIED. I REFUSE TO ANSWER. BECAUSE I DONT WANT TO. NEXT. YOU HAVE BEEN STOPPED."
  alert = discord.Embed(title="PERMISSION DENIED", description=desc, url="https://youtu.be/tA8LjcpjjKQ")
  alert.set_thumbnail(url="https://cdn.discordapp.com/attachments/944164645818744922/947864753026506812/gowk6neidu831.png")
  await message.channel.send(embed=alert)