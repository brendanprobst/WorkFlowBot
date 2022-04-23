import yaml
import os

from themes import color
import commands

# The line below is required on Windows for
# color formatting on default command prompt
os.system("color")

prompt = ">"


with open("config.yml", "r") as stream:
    data = yaml.safe_load(stream)
# Use the presets variable below globally
presets = data["presets"]
# The username variable grabs the username of the current user on Windows
username = os.getlogin()
for preset in presets:
    for program in presets[preset]:
        if "SYS_USERNAME" in program[1]:
            program[1] = str(program[1]).replace("SYS_USERNAME", username)


def executeCommand(commandArr):
    """
    Takes a string cmd and executes the appropriate function.
    This function essentially maps user inputted commands to
    their corresponding function in the code.
    """
    with open("config.yml", "r") as stream:
        data = yaml.safe_load(stream)
    presets = data["presets"]
    cmd = commandArr[0]
    args = []
    if len(commandArr) > 1:
        args = commandArr[1:]
    print("")
    if cmd == "help":
        commands.helpCmd(args)
    elif cmd == "list":
        commands.listCmd(args, presets)
    elif cmd == "wob":
        commands.wobCmd(args, presets)
    elif cmd == "new":
        commands.newTemplateCmd(args)
    else:
        print("That command is valid, but not yet implemented.")


def isValidCommand(command):
    commandArr = command.split()
    if not commandArr or commandArr[0] not in commands.allowedCmds:
        print(color("Invalid command. Type 'help' for a list of commands.", "FAIL"))
    else:
        return True


# Initialize WOBot
print(color("==============================================", "OKCYAN"))
print(color(" Welcome to WOBot - Workflow Organization Bot", "OKCYAN"))
print(color("==============================================", "OKCYAN"))

userInput = ""

print("Type", color("wob <preset-name>", "WARNING"), "to open a preset.")
print("Example:")
print(">wob work")
print("Or, type 'help' for a list of commands.")
print("Type 'help' <command name> for usage of commands.\n")

while userInput != "quit":

    userInput = input(prompt)
    # TODO: prints after you type quit - figure out how to prevent that
    # print("Running command: " + userInput)
    if isValidCommand(userInput):
        # Sends user input to executeCommand as an array
        # executeCommand separates the input into the base
        # command and an array of args
        executeCommand(userInput.split())
