class CommandManager:

    def __init__(self):
        self.registered_commands = []

    def register_command(self, command):
        self.registered_commands.append(command)

    def wait_for_command_input(self):
        gib_was_ein = input("Bitte gib einen command ein ")
        name = gib_was_ein.split(" ")[0]
        args = []
        if name != gib_was_ein:
            args = gib_was_ein.replace(name + " ", "").split(" ")
        for command in self.registered_commands:
            if command.name == name:
                command.call(args)
                break


class Command:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def call(self, args):
        pass
