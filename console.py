#!/usr/bin/python3
"""Model for console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "

    def quit(self, line):
        """exit the program"""
        return True

    def EOF(self, line):
        """exit the program , end of file."""
        return True

    def empty_line(self):
        """Do nothing when an empty line is entered."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
