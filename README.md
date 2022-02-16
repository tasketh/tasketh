# tasketh

[![Build Status](https://img.shields.io/badge/Build-Passing-<>.svg)](https://shields.io/) [![Maintained](https://img.shields.io/badge/Maintained-darkgreen.svg)](https://shields.io/) 

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Release](https://img.shields.io/badge/Release-v1.0.0-blue.svg)](https://shields.io/) [![Python 3.6](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)

![](https://cdn.discordapp.com/attachments/942689663150342184/943415314203414578/unknown.png) 


tasketh is a simple bot that lets users claim tasks. As of now, tasketh specialises only in task claiming but there's lots on the way!

## Process
- When a task is announced, it sends an embed specifying details of the task, number of people required for the task and more.
- Users who want to claim the task will do so by reacting to the embed.
- Once the task has been claimed by the specified number of people, the claiming closes.
- A report consisting of the list of users who have claimed the task will be sent in the configured channel. The user list will be sorted according to time.
- The report will mention the users so that the task supervisor can add roles if required. 
- In case of any concerns about users reacting by mistake or users dropping tasks after claiming it, a suitable buffer can be set so that extra responses will be taken.

## Potential features

- Provide option for changing prefix.
- Add more commands to manage tasks.
- Record all responses in a database.
- Work on customising the bot for other servers.
- Dashboard.

## License
This project is licensed under the GNU General Public License v3.0 -check [LICENSE.md] (https://github.com/GHrohith/tasketh/blob/main/LICENSE) for more details.


## Development

Want to contribute? Great!
Fork this repository and create a pull request.


