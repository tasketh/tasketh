import discord

from rudder import pretty


async def helpeth(message, server):
    help_tasketh = discord.Embed(
        title=(
            "This is tasketh! A simple discord bot that lets moderators assign,"
            "and users claim tasks. Here are details about all commands"
        ),
        color=pretty,
    )
    # help_tasketh.set_thumbnail(url=server.logo)
    help_tasketh.set_footer(text="Help on tasketh", icon_url=server.logo)
    await message.channel.send(
        embed=help_tasketh, reference=message, mention_author=False
    )


async def status(message, server):
    print("tasketh state")
    reply = discord.Embed(
        title="Current status of tasketh",
        description=f"""
        tasketh prefix: `{server.prefix}`
        Role with permissions to use all commands: <@&{server.permitted}>
        Role pinged when task is announced: {server.taskMention}
        Channel that receives tasks: <#{server.taskschannel}>
        Channel that receives reports: <#{server.reportschannel}>
        Number of buffer user responses considered: `{server.bufferUsers}`""",
    )
    reply.set_footer(
        text=f"Use the command `{server.prefix}help` for help on all tasketh commands",
        icon_url=server.logo,
    )
    await message.channel.send(embed=reply, reference=message, mention_author=False)
