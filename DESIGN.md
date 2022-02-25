WOBot
WorkFlow Organization Bot
Brendan Probst, Amit Bhatnagar, Christian Huang

Problem Statement

The problem is that power users typically have multiple applications open at once and it becomes difficult to keep all the windows and desktops organized. When a user has multiple desktops open, it gets even harder to keep things organized. Also, organizing windows when you have multiple monitors is tedious and takes time. This is also a problem because when a user wants to switch workflows (switch from meeting mode to coding mode for example). 

This is a major problem because it slows people down and hurts productivity. It also taxes people's minds when they have to constantly, manually, open and close windows throughout the day. I often find myself keeping unnecessary windows open throughout the day because I know I’m going to need to come back to them and don’t want to go through the hassle of opening and closing them again. Additionally, having many programs open at the same time is harmful to computer hardware and accelerates performance deterioration. 



Bot Description

This bot will operate from the user’s command line. This is a good solution for our problem because we are targeting this primarily at programmers (us) who are already comfortable with the command line. The way this bot will operate is by opening when the computer boots up, and when the terminal sees the appropriate command at the beginning of a line, it will activate, and then listen for the next word or string of words. When the user presses enter, it will either execute the command or return an error message. 

The bot will not have a conversation with users but instead, respond with validation or error messages after each command and list additional information when the user prompts for help. 
The bot will not have any analytical features, just respond to inputs given by the user. 

WOBot - Organize Your Windows


Use Cases:

Use Case: Create a custom template of applications

1 Precondition

   Program has permissions to read local files

2 Main Flow

User open all the applications that they want to have in the custom template and names the template [S1]. Bot scans user’s system processes and lists them in a config file [S2]. If Google Chrome is one of the listed apps, bot reminds user to fill out custom urls in config file [S3]. User checks config file and makes edits as necessary [S4].

3 Subflows

  [S1] User opens the desired applications, and the bot will write all processes to the config under the specified template name.
  [S2] Bot scans the users computer for open processes.
  [S3] Bot checks if Google Chrome is open and if it is, reminds user to input URLs.
  [S4] User creates the custom template and data is saved to the config file.

4 Alternative Flows

  [E1] User opens an app that can’t be automatically opened by the bot.
  [E2] Bot can’t identify an application the user wants in their template..
  [E3] Bot does not detect Google Chrome.
  [E4] Bot misidentifies a process. 
  
Use Case: Open a template

1 Precondition

   User has at least one template stored. Program has permissions to read/write local files.

2 Main Flow

User chooses either a premade or custom template from their list of templates [S1]. Bot will close all open applications on the computer [S2]. Bot will open all of the applications listed in the template [S3].
 
3 Subflows

  [S1] User selects a template consisting of the processes they want open.

  [S2] Bot closes the applications.

  [S3] Bot will open all the application in the template. 

4 Alternative Flows

  [E1] User 

  [E1] Bot can’t close an application.

  [E1] Bot can’t open an application listed in the template.

Design Sketches
For pictures see /designPictures


Architecture Design
For picture see /designPictures



The architecture for the WOBot is very simple. The main functionality will be housed in a Python script, which will interact with the external applications that the bot scans. To control the bot, the user will interact with a command-line interface that uses the Python script. To determine the programs that should be opened/closed, the Python script will refer to the workflow.config.json file, which stores information about application presets for different workflow templates.


