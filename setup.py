# set_logo, set_buffer, set_taskschannel, set_reportschannel, help commands, set reaction emote
import discord
from custom import *

async def setPrefix(message, value):
  """-prefix <new prefix> """
  #Check this loop
  if 3>len(value)>=1:
    global PREFIX
    PREFIX = value
    prefixEmbed = discord.Embed(title=f"Prefix changed to {PREFIX}")
    await message.channel.send(embed=prefixEmbed)
  else:
    prefixEmbed = discord.Embed(title="Error", description="Prefix cannot be longer than 3 characters")
    await message.channel.send(embed=prefixEmbed)
  
  


def setTaskChannel(message, value):
  """ """
  pass
  
def setReportChannel(message, value):
  """ """
  pass
  

