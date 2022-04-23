import yaml
from tkinter import Tk 
from tkinter.filedialog import askopenfilenames
import os
from themes import color
allowedCmds = {
    # Keep adding to this dictionary
    # If the command requires no args,
    # simply enter the usage as ""
    "help": {
        "usage": "help [command]",
        "description": "Returns the list of commands and their basic usage. Optionally takes a command as an arg for help on a specific command.",
    },
    "list": {
        "usage": "list [preset]",
        "description": "Lists all presets. Optionally takes a preset as an arg to list programs for a specific preset."
    },
    "wob": {
        "usage": "wob <preset>",
        "description": "Opens the programs in a preset and closes other programs."
    },
    "new": {
        "usage": "wob <preset>",
        "description": "Opens the programs in a preset and closes other programs."
    },
}


def usageError(command, message="Too many args provided!"):
    """
    Prints an error message and the usage for the given command.
    By default, the error says 'Too many args provided!'.
    An optional second argument (string) can be used to override
    this message with a different one.
    """
    print(message)
    print(color("Usage: " + allowedCmds[command]['usage'], "WARNING"))


def helpCmd(args):
    if(not args):
        # No argument provided, list all commands
        for key, value in allowedCmds.items():
            print(color(key + " -", "HEADER"), value['description'])
    elif len(args) == 1:
        # Provide usage and description for specific command
        if(args[0] in allowedCmds):
            # If command exists, print command name and description
            print(color(args[0] + ":", "HEADER"),
                  allowedCmds[args[0]]['description'])
            if(allowedCmds[args[0]]['usage']):
                # Check if the command has a "usage" field. If so, print it.
                print(
                    color("Usage: " + allowedCmds[args[0]]['usage'], "WARNING"))
        else:
            print(color("No command named '" + args[0] + "' exists.", "FAIL"))
    else:
        usageError("help")


def listCmd(args, presets):
    if(not args):
        # No argument provided, list all presets
        print(color("These are your accessible Presets", "OKCYAN"))
        for preset in presets:
            print(color(preset + ":", "OKGREEN"))
            for program in presets[preset]:
                # Break each program of a particular preset into its name and path
                programName, path = program
                print("\t" + programName)
                # print("\t\t" + path)
    elif len(args) == 1:
        if args[0] in presets:
            # If preset provided exists
            for program in presets[args[0]]:
                # Break each program of a particular preset into its name and path
                programName, path = program
                print(color(programName, "OKGREEN"))
                # print(color("\t" + path, "OKGREEN"))
        else:
            # Preset doesn't exist
            print(color("No preset named '" + args[0] + "' exists.", "FAIL"))
    else:
        usageError("list")


def wobCmd(args, presets):
    if(not args):
        usageError("wob", "No args provided.")
    elif len(args) == 1:
        if args[0] in presets:
            
            # If preset provided exists
            for program in presets[args[0]]:

                # Break each program of a particular preset into its name and path
                programName, path = program
                print(color("Starting '" + programName + "'...", "OKBLUE"))
                os.startfile(path)
        else:
            # Preset doesn't exist
            print(color("No preset named '" + args[0] + "' exists.", "FAIL"))
    else:
        usageError("wob")

def newTemplateCmd(args):
    tempName = args[0]
    Tk().withdraw()
    print("Naviagte to the file selector that has opened and select all programs you would like in the template.")
    path = askopenfilenames()
    pathNames = []
    for thePath in path:
        pathNames.append(os.path.split(thePath)[1])
    with open("config.yml") as stream:
        data = yaml.safe_load(stream)
        data["presets"][tempName] = []
        temp = []
        for num in range(len(pathNames)):
            temp.append([pathNames[num], path[num]])
        data["presets"][tempName] = temp

    with open("config.yml", "w") as stream:
        yaml.dump(data, stream)
    print("Template with name:", tempName, "created! Please re-launch to use the template.")
    

