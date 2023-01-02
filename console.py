#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """Console module."""
    
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        """exit the interpreter."""
        return True

    def do_EOF(self, line):
        """exit by clicking Ctrl-D."""
        return True

    def postloop(self):
        """print a new line after interpreter is exited."""
        print()

    def help_quit(self):
        """doc for the quit command."""
        print("Quit command to exit the interpreter.\n")

    def help_EOF(self):
        """doc for EOF command."""
        print("Exits the interpreter when Crtl-D is pressed.\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
