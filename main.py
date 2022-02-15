import discord
import os
from custom import *
from tasks import *


client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  """Function called when a message is sent"""
  if message.author == client.user:           #checks if the message is sent by the bot
    return

  #task command
  if message.content.startswith(PREFIX+"task "): #task command  
    #Separates the command and assigns them to the dictionary.
    commandList = message.content[len(PREFIX)+4::].strip().split(SYNTAX_DELIMITER)
    taskDetails = {'taskUsers':int(commandList[0]), 'taskHours':commandList[1], 'taskName':SYNTAX_DELIMITER.join(commandList[2::])}
  
    sentTaskMsg = await sendTaskEmbed(message, client, taskDetails)

    userList = await collectResponses(sentTaskMsg, client, taskDetails)

    await closeTask(sentTaskMsg, taskDetails)

    await sendReport(client, taskDetails, userList)


client.run(os.getenv('TOKEN'))
