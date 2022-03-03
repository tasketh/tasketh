import discord

from tasks import *
from rudder import *
from about import *


client = discord.Client()

task = "task "
testtask = "testtask "

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_guild_join(joinedGuild):
    # it will forget previous configs if bot is re-added into a server
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

    if message.content.startswith(serverPrefix) or message.content == "tasketh-state":
        try:
            server
        except NameError:
            server = getServerConfigs(message.guild.id)
        finally:
            if message.content == "tasketh-state":
                await status(message, server)
    else:
        return

    # checks if the message is sent by the bot
    if message.author == client.user:
        return

    roles = [role.id for role in message.author.roles]

    if message.content.startswith(serverPrefix + "permit"):
        """Gives task sending permission to the mentioned role"""
        if message.author.guild_permissions.administrator:
            await permit(message, server)
        else:
            await permDenied(message)

    elif message.content.startswith(serverPrefix + task):
        """Task command"""
        if (message.author.guild_permissions.administrator) or (server.permitted in roles):

            # if task and report channel is'nt set up, then throw an error
            if None in (server.taskschannel, server.reportschannel):
                alert = discord.Embed(
                    title="Alert",
                    description="Channel ID for tasks and reports haven't been configured. Please use the help command and configure them",
                )
                await message.channel.send(embed=alert)

            else:
                taskDetails = details(message, server, len(task))
                sentTaskMsg = await sendTaskEmbed(message, client, taskDetails, server)
                await message.add_reaction(server.reactEmoji)
                userList = await collectResponses(
                    sentTaskMsg, client, taskDetails, server
                )
                await closeTask(sentTaskMsg, taskDetails, server)
                await sendReport(client, taskDetails, userList, server)
        else:
            await permDenied(message, server)

    elif message.content.startswith(serverPrefix + testtask):
        """Test task command that sends a preview of the task emebed"""
        if (message.author.guild_permissions.administrator) or (server.permitted in roles):
            # if task and report channel is'nt set up, then throw an error
            if None in (server.taskschannel, server.reportschannel):
                alert = discord.Embed(
                    title="Alert",
                    description="Channel ID for tasks and reports haven't been configured. Please use the help command and configure them",
                )
                await message.channel.send(embed=alert)

            else:
                taskDetails = details(message, server, len(testtask))
                await testTask(message, taskDetails, server)
        else:
            await permDenied(message, server)

    elif message.content.startswith(serverPrefix + "taskmention"):
        """Syntax: <prefix>taskmention <role>"""
        await check(message, server, setMentionRole)

    elif message.content.startswith(serverPrefix + "taskchannel"):
        """Sets the channel to send tasks in"""
        await check(message, server, setTasksChannel)

    elif message.content.startswith(serverPrefix + "reportchannel"):
        """Sets the channel to send reports in"""
        await check(message, server, setReportsChannel)

    elif message.content.startswith(serverPrefix + "prefix"):
        """Syntax: <current prefix>prefix <oldprefix>"""
        await check(message, server, setPrefix)

    elif message.content.startswith(serverPrefix + "bufferusers"):
        """Syntax: <current prefix>bufferusers <custom number of buffer users>"""
        await check(message, server, setBuffer)

    elif message.content == f"{serverPrefix}help":
        await helpeth(message, server)


client.run(config("BOT_TOKEN"))
