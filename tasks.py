import discord

from rudder import pretty

taskFooter = (
    "Please keep in mind that tasks are assigned on a first come, first served basis."
)


async def sendTaskEmbed(message, client, taskDetails, server):
    """Uses the message object and task details to anounce a task"""
    # Sends the task message and assigns its id to sentTaskMsg
    taskDesc = f"Number of people required: **{taskDetails['taskUsers']}**\nNumber of hours: **{taskDetails['taskHours']}**"
    taskEmbed = discord.Embed(
        title=f"New Task! {taskDetails['taskName']}",
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


async def collectResponses(TaskMsg, client, taskDetails, server):
    """Adds user ID of each reaction to userList until length of userList reaches specified number of users+buffer"""

    def check(reaction, user):
        """Returns true if a user other than the bot reacts with the correct emoji to the task message"""
        return (
            user != client.user
            and reaction.message == TaskMsg
            and str(reaction.emoji) == server.reactEmoji
        )

    userList = []
    resUsers = taskDetails["taskUsers"] + server.bufferUsers
    while len(userList) < resUsers:
        reaction, user = await client.wait_for("reaction_add", check=check)
        userId = user.id
        userList.append(userId)

    return userList


async def closeTask(TaskMsg, taskDetails, server):
    await TaskMsg.clear_reactions()
    closedTaskName = "Task Closed"
    closedTaskDesc = (
        taskDetails["taskName"]
        + f"\nNumber of people required: {taskDetails['taskUsers']}\nNumber of hours: {taskDetails['taskHours']}"
    )
    closedTaskEmbed = discord.Embed(title=closedTaskName, description=closedTaskDesc)
    closedTaskEmbed.set_thumbnail(url=server.logo)
    closedTaskEmbed.set_footer(text=taskFooter)
    await TaskMsg.edit(embed=closedTaskEmbed)


async def sendReport(client, taskDetails, userList, server):
    reportDesc = ""
    reportFooter = "Responses are sorted according to time."

    for i in range(len(userList)):
        reportDesc += f"{str(i+1)}. <@{userList[i]}>\n"

    report = discord.Embed(
        title=f"Report for \"{taskDetails['taskName']}\"",
        description=reportDesc,
        color=pretty,
    )
    report.set_footer(text=reportFooter, icon_url=server.logo)
    await client.get_channel(server.reportschannel).send(embed=report)
