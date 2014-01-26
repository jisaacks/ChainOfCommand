import sublime
import sublime_plugin

class ChainCommand(sublime_plugin.WindowCommand):
    def run(self, commands):
        window = self.window
        for command in commands:
            command_name = command[0]
            command_args = command[1:]
            window.run_command(command_name, *command_args)
