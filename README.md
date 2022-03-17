<p align="center">
  <img src="https://raw.githubusercontent.com/GHrohith/tasketh/main/Assets/icon.png" alt="tasketh" width="100" height="100">
  <br>
  <h1 align="center"><b>tasketh</b></h1>
  <p align="center">
  <b>Maintainers</b>
  </p>
  <p align="center">
  <table align='center'>
    <tr align='center' rules='none'>
      <td>
        <a href="https://github.com/GHrohith"><img src="https://avatars.githubusercontent.com/u/84242221?v=4" alt="GHrohith" width="50" height="50"></a> 
      </td>
      <td>
         <a href="https://github.com/samhitha-b"><img src="https://avatars.githubusercontent.com/u/71536982?v=4" alt="samhitha-b" width="50" height="50"></a> 
      </td> 
    </tr>
    <tr>
      <td>
        <a href="https://github.com/GHrohith">Rohith</a>
      </td> 
      <td>
        <a href="https://github.com/samhitha-b">Samhitha</a>
      </td>  
    </tr>  
  </table>
</p>



[![Build Status](https://img.shields.io/badge/Build-Passing-<COLOR>.svg)](https://shields.io/) [![Maintained](https://img.shields.io/badge/Maintained-darkgreen.svg)](https://shields.io/)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Generic badge](https://img.shields.io/badge/Release-v1.0.0-<COLOR>.svg)](https://shields.io/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)



tasketh is a simple bot that lets users claim tasks. As of now, tasketh specialises only in task claiming but there's lots on the way!

## Process
- After the bot is invited to a server, the task and report embedding channels must be set using the required commands `!taskchannel` and `!reportchannel`.
- When a task is announced using the `!task` command, it sends an embed specifying details of the task, number of people required for the task and more.
- Users who want to claim the task will do so by reacting to the embed.
- Once the task has been claimed by the specified number of people, the claiming closes.
- A report consisting of the list of users who have claimed the task will be sent in the configured channel. The user list will be sorted according to time.
- The report will mention the users so that the task supervisor can add roles if required. 
- In case of any concerns about users reacting by mistake or users dropping tasks after claiming it, a suitable buffer can be set so that extra responses will be taken.

## Features
- The task channel and report channel can be set individually
- Admins can permit a role to use all commands
- Custom number of buffer users can be configured 
- Task can be closed manually before the sufficient number of people have reacted
- Permitted users can request for a preview of the task embed before sending it
- The help command can be used for details about all commands
- *tasketh-state* command can be used to view the current settings of the bot

## Screenshots
![Screenshot of a test case](https://github.com/GHrohith/tasketh/blob/main/Screenshots/tasketh.png?raw=true&sanitize=true "screenshot")

## Potential features
- Option for responders to be given certain roles/added to a new channel/sent task details as a direct message.
- Add more commands to manage tasks.
- Dashboard.

## License
This project is licensed under the GNU General Public License v3.0. Check [LICENSE.md](https://github.com/GHrohith/tasketh/blob/main/LICENSE) for more details.

## Attribution
- [Icon: ](httphttps://github.com/GHrohith/tasketh/blob/main/Assets/icon.png:// "Icon: ") <a href="https://www.flaticon.com/free-icons/art-and-design" title="art and design icons">Art and design icons created by Freepik - Flaticon</a>

## Acknowledgements
- [python-decouple](https://github.com/henriquebastos/python-decouple/ "python-decouple")
- [pickle](https://github.com/python/cpython "pickle")

## Development

Want to contribute?
Fork this repository and create a pull request.
