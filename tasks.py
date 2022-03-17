import discord

from rudder import pretty, permission

taskFooter = (
    "Please keep in mind that tasks are assigned on a first come, first served basis."
)


def details(message, server, n):
    # Separates the command and assigns them to the dictionary.
    commandList = (
        message.content[len(server.prefix) + n : :]
        .strip()
        .split(server.syntaxDelimiter)
    )
    taskDetails = {
        "taskUsers": commandList[0].strip(),
        "taskHours": commandList[1].strip(),
        "taskName": server.syntaxDelimiter.join(commandList[2::]).strip(),
    }
    return taskDetails


async def sendTaskEmbed(client, taskDetails, server):
    """Uses the message object and task details to anounce a task"""
    # Sends the task message and assigns its id to sentTaskMsg
    taskDesc = f"**{taskDetails['taskName']}**\n\nNumber of people required: **{taskDetails['taskUsers']}**\nNumber of hours: **{taskDetails['taskHours']}**"
    taskEmbed = discord.Embed(
        title=f"New Task!",
        description=taskDesc,
        color=0x67D129,
    )
    taskEmbed.set_thumbnail(url=server.logo)
    taskEmbed.set_footer(text=taskFooter)
    sentTaskMsg = await client.get_channel(server.taskschannel).send(
        content=f"{server.taskMention}", embed=taskEmbed
    )
    await sentTaskMsg.add_reaction(server.reactEmoji)

    return sentTaskMsg


async def testTask(message, taskDetails, server):
    """Uses the message object and task details to anounce a task"""
    # Sends the task message and assigns its id to sentTaskMsg
    taskDesc = f"**{taskDetails['taskName']}**\n\nNumber of people required: **{taskDetails['taskUsers']}**\nNumber of hours: **{taskDetails['taskHours']}**"
    taskEmbed = discord.Embed(
        title=f"New Task!",
        description=taskDesc,
        color=0x67D129,
    )
    taskEmbed.set_thumbnail(url=server.logo)
    taskEmbed.set_footer(text=taskFooter)
    await message.channel.send(
        content="This is a preview.",
        embed=taskEmbed,
        reference=message,
        mention_author=False,
    )


async def collectResponses(TaskMsg, client, taskDetails, server):
    """Adds user ID of each reaction to userList until length of userList reaches specified number of users+buffer"""

    def check(reaction, user):
        """Returns true if a user other than the bot reacts with the correct emoji to the task message"""
        return (
            user != client.user
            and reaction.message == TaskMsg
            and str(reaction.emoji) in [server.reactEmoji, '❌']
        )

    userList = []
    resUsers = int(taskDetails["taskUsers"]) + server.bufferUsers
    while len(userList) < resUsers:
        reaction, user = await client.wait_for("reaction_add", check=check)

        if reaction.emoji==server.reactEmoji:
            userId = user.id
            if userId in userList:
                userList.remove(userId)
            userList.append(userId)
        elif reaction.emoji=='❌' and permission(user, server):
            break

    return userList


async def closeTask(TaskMsg, taskDetails, server):
    await TaskMsg.clear_reactions()
    closedTaskName = "Task Closed"
    closedTaskDesc = (
        taskDetails["taskName"]
        + f"\n\nNumber of people required: {taskDetails['taskUsers']}\nNumber of hours: {taskDetails['taskHours']}"
    )
    closedTaskEmbed = discord.Embed(title=closedTaskName, description=closedTaskDesc)
    closedTaskEmbed.set_thumbnail(url=server.logo)
    closedTaskEmbed.set_footer(text=taskFooter)
    await TaskMsg.edit(embed=closedTaskEmbed)


async def sendReport(client, taskDetails, userList, server):
    reportDesc = f"Task: {taskDetails['taskName']}\n\n"
    for i in range(len(userList)):
        reportDesc += f"{str(i+1)}. <@{userList[i]}>\n"

    reportFooter = "Responses are sorted according to time."

    report = discord.Embed(
        title="Report",
        description=reportDesc,
        color=pretty,
    )
    report.set_footer(text=reportFooter, icon_url=server.logo)
    await client.get_channel(server.reportschannel).send(embed=report)
