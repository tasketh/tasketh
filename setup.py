import discord
import pymongo
from decouple import config
from server import *

client = pymongo.MongoClient(config("CLUSTER_URL"))
collection = client.tasketh.guilds

cache = {}


def getServerConfigs(serverid):
  """returns the dictionary that contains server configuration"""

  result = collection.find_one({"Server":serverid})
  cache[result["Server"]] = result["Prefix"]

  server = Server(serverid)
  server.prefix = result["Prefix"]
  server.syntaxDelimiter = result["syntaxDelimiter"]
  server.bufferUsers = result["Buffer"]
  server.logo = result["Logo"]
  server.taskschannel = result["TasksChannel"]
  server.reportschannel = result["ReportsChannel"]
  server.taskMention = result["TaskMention"]
  server.permitted = result["Permitted"]
  server.reactEmoji = result["Emoji"]

  return server


def updateServerConfigs(server):
  """Updates the server configuration"""
  ind = {"Server":server.id}
  dic = {"$set": 
          {
            "Prefix":server.prefix, 
            "syntaxDelimiter":server.syntaxDelimiter, 
            "Buffer":server.bufferUsers, 
            "Logo":server.logo, 
            "TasksChannel":server.taskschannel, 
            "ReportsChannel": server.reportschannel, 
            "TaskMention": server.taskMention,
            "Permitted": server.permitted,
            "Emoji":server.reactEmoji
          }
        }

  collection.update_one(ind, dic, upsert=True)


async def setPrefix(message, server):
  """Changes prefix of tasketh in a particular server
  Syntax: <current prefix>prefix <oldprefix>"""
  value = message.content.split()[-1]
  if 3>len(value)>=1:
    server.prefix = value
    updateServerConfigs(server)
    cache[server.id]=value
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