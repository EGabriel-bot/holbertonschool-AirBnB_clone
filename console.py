#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        exit()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
