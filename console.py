#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_create(self, args):
        'Creates a new instance of BaseModel, saves it (to the JSON file)\n'
        if not args:
            print("** class name missing **")
        if args != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            #json.dump(new, file.json)
            print(new.id)

    def do_show(self, *args):
        'Prints the string representation of an instance based on the class name and id\n'
        new = BaseModel()
        #arg = args.split()
        if not args[0]:
            print("** class name missing **")
        elif args[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 1 or args[1] != new.id:
            print("** no instance found **")
        else:
            print(args)

   # ------------- PreCmd and PostCmd -------

    """
    def precmd(self, line):
        line = line.lower()
        if self.file:
            print(line, file=self.file)
        return line
    """

    def postcmd(self, stop, line):
        if cmd.Cmd.do_help:
            HBNBCommand().cmdloop()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
