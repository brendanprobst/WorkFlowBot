from themes import color

allowedCmds = {
    # Keep adding to this dictionary
    # If the command requires no args,
    # simply enter the usage as ""
    "wob": {
        "usage": "wob <preset>",
        "description": "Opens the programs in a preset and closes other programs."
    },
    "list": {
        "usage": "list [preset]",
        "description": "Lists all presets. Optionally takes a preset as an arg to list programs for a specific preset."
    },
    "help": {
        "usage": "help [command]",
        "description": "Returns the list of commands and their basic usage. Optionally takes a command as an arg for help on a specific command.",
    }}


def tooManyArgs(command):
    print("Too many args provided!")
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
        tooManyArgs("help")


def listCmd(args, presets):
    if(not args):
        # No argument provided, list all presets
        print(color("These are your accessible Presets", "OKCYAN"))
        for preset in presets:
            print(color(preset + ":", "OKGREEN"))
            for program in presets[preset]:
                print("\t" + program)
    elif len(args) == 1:
        # If preset provided exists
        if args[0] in presets:
            for program in presets[args[0]]:
                print(color(program, "OKGREEN"))
        else:
            # Preset doesn't exist
            print(color("No preset named '" + args[0] + "' exists.", "FAIL"))
    else:
        tooManyArgs("list")
