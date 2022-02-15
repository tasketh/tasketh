from custom import *
import discord
""" """

taskFooter = "Please keep in mind that tasks are assigned on a first come, first served basis."


async def sendTaskEmbed(message, client, taskDetails):
  """Uses the message object and task details to anounce a TASK_CHANNEL"""
  #Sends the task message and assigns its id to sentTaskMsg
  taskDesc = f"Number of people required: **{taskDetails['taskUsers']}**\nNumber of hours: **{taskDetails['taskHours']}**"
  
  taskEmbed = discord.Embed(title=f"New Task! {taskDetails['taskName']}",description= taskDesc, color=0x67d129)
  taskEmbed.set_thumbnail(url=LOGO)
  taskEmbed.set_footer(text=taskFooter)
  sentTaskMsg = await client.get_channel(TASK_CHANNEL).send(content=TASK_MENTION, embed=taskEmbed)
  await sentTaskMsg.add_reaction(REACT_EMOJI)
  
  return sentTaskMsg


async def collectResponses(TaskMsg, client, taskDetails):
  #Adds userid of each reaction to userList until length of userList rea
  def check(reaction, user):
    """Returns true if a user other than the bot reacts with the correct emoji to the task message"""
    return user!=client.user and reaction.message==TaskMsg and str(reaction.emoji) == REACT_EMOJI

  userList = []
  resUsers = taskDetails['taskUsers'] + BUFFER_PPL
  while len(userList)<resUsers:
    reaction, user = await client.wait_for('reaction_add', check=check)
    userId = user.id
    userList.append(userId)

  return userList


async def closeTask(TaskMsg, taskDetails):
  await TaskMsg.clear_reactions()
  closedTaskName = "Task Closed"
  closedTaskDesc = taskDetails['taskName'] + f"\nNumber of people required: {taskDetails['taskUsers']}\nNumber of hours: {taskDetails['taskHours']}"
  closedTaskEmbed = discord.Embed(title=closedTaskName,description= closedTaskDesc)
  closedTaskEmbed.set_thumbnail(url=LOGO)
  closedTaskEmbed.set_footer(text=taskFooter)
  await TaskMsg.edit(embed=closedTaskEmbed)


async def sendReport(client, taskDetails, userList):
  reportDesc =  ""
  reportFooter = "Responses are sorted according to time."

  for i in range(len(userList)):
    reportDesc+=(f'{str(i+1)}. <@{userList[i]}>\n')

  report = discord.Embed(title=f"Report for \"{taskDetails['taskName']}\"", description=reportDesc)
  report.set_footer(text=reportFooter, icon_url=LOGO)
  await client.get_channel(REPORT_CHANNEL).send(embed=report)
