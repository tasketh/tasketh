import discord
import os

#CUSTOM VARIABLES
task_channel = 942690426920529930
react_emoji = '✅'
task_command = '!@task '
syntax_delimiter = '|'
task_mention = '@123here'
report_channel = 942730050531369069
buffer_ppl = 0
logo = "https://cdn.discordapp.com/attachments/876497372228759562/941687088624054343/29996451.png"
#END OF CUSTOM VARIABLES

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith(task_command):
    commandContent = message.content[len(task_command)::]
    commandList = commandContent.split(syntax_delimiter)
    numPplOg = int(commandList[0])
    numHrs = commandList[1]
    taskName = syntax_delimiter.join(commandList[2::])
    taskDesc = f"Number of people required: **{numPplOg}**\nNumber of hours: **{numHrs}**"
    taskFooter = "Please keep in mind that tasks are assigned on a first come, first served basis."
    taskEmbed = discord.Embed(title=f"New Task! {taskName}",description= taskDesc)
    taskEmbed.set_thumbnail(url=logo)
    taskEmbed.set_footer(text=taskFooter)

    sentMsg = await client.get_channel(task_channel).send(content=task_mention, embed=taskEmbed)

    await sentMsg.add_reaction(react_emoji)

    userList = []
    numPpl = numPplOg + buffer_ppl
    
    def check(reaction, user):
      return str(reaction.emoji) == react_emoji and user!=client.user

    while len(userList)<numPpl:
      reaction, user = await client.wait_for('reaction_add', check=check)
      if reaction.message!=sentMsg:
        continue
      userId = user.id
      userList.append(userId)

    await sentMsg.clear_reactions()
    closedTaskName = "Task Closed"
    closedTaskDesc = taskName + f"\nNumber of people required: {numPplOg}\nNumber of hours: {numHrs}"
    closedTaskEmbed = discord.Embed(title=closedTaskName,description= closedTaskDesc)
    taskEmbed.set_thumbnail(url =logo)
    taskEmbed.set_footer(text=taskFooter)
    await sentMsg.edit(embed=closedTaskEmbed)

    reportDesc =  ""
    reportFooter = "Responses are sorted according to time."

    for i in range(len(userList)):
      reportDesc+=(f'{str(i+1)}. <@{userList[i]}>\n')

    report = discord.Embed(title=f"Report for {taskName}", description=reportDesc)
    report.set_footer(text=reportFooter, icon_url =logo)
    await client.get_channel(report_channel).send(embed=report)



client.run(os.getenv('TOKEN'))

