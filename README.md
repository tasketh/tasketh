# tasketh

[![Build Status](https://img.shields.io/badge/Build-Passing-<COLOR>.svg)](https://shields.io/) [![Maintained](https://img.shields.io/badge/Maintained-darkgreen.svg)](https://shields.io/)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Generic badge](https://img.shields.io/badge/Release-v1.0.0-<COLOR>.svg)](https://shields.io/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

![](https://cdn.discordapp.com/attachments/942689663150342184/943415314203414578/unknown.png)


tasketh is a simple bot that lets users claim tasks. As of now, tasketh specialises only in task claiming but there's lots on the way!

## Process
- After the bot is invited to a server, the task and report embedding channels must be set using the required commands `!taskchannel` and `!reportchannel`.
- When a task is announced using the `!task` command, it sends an embed specifying details of the task, number of people required for the task and more.
- Users who want to claim the task will do so by reacting to the embed.
- Once the task has been claimed by the specified number of people, the claiming closes.
- A report consisting of the list of users who have claimed the task will be sent in the configured channel. The user list will be sorted according to time.
- The report will mention the users so that the task supervisor can add roles if required. 
- In case of any concerns about users reacting by mistake or users dropping tasks after claiming it, a suitable buffer can be set so that extra responses will be taken.

## Screenshots

![Screenshot of a test case](https://github.com/GHrohith/tasketh/blob/main/Screenshots/tasketh.png?raw=true&sanitize=true "screenshot")

## New Features
- Custom prefix, number of buffer users and other settings for each server.


## Potential features
- Help command.
- Option for responders to be given certain roles/added to a new channel/send task details as a direct message.
- Create command `!testtask` that will send a preview of the task embed.
- Add more commands to manage tasks.
- Add a command that will display the current state of all custom settings.
- Record all responses in a database.
- Dashboard.

## License
This project is licensed under the GNU General Public License v3.0 -check [LICENSE.md] (https://github.com/GHrohith/tasketh/blob/main/LICENSE) for more details.

## Attribution
- [Icon: ](httphttps://github.com/GHrohith/tasketh/blob/main/Assets/icon.png:// "Icon: ") <a href="https://www.flaticon.com/free-icons/art-and-design" title="art and design icons">Art and design icons created by Freepik - Flaticon</a>

## Acknowledgements
- [python-decouple](https://github.com/henriquebastos/python-decouple/ "python-decouple")
- [pickle](https://github.com/python/cpython "pickle")

## Development

Want to contribute?
Fork this repository and create a pull request.