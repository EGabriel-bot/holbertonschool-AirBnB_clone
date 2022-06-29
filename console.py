#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, args):
        'Quit command to exit the program\n'
        exit()

    def do_EOF(self, args):
        'EOF command to exit the program\n'
        exit()

    def do_create(self, args):
        'Creates a new instance of BaseModel, saves it (to the JSON file)\n'
        if not args:
            print("** class name missing **")
        elif args != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        'Prints the string representation of an instance based on the class name and id\n'
        rep = storage.all()
        arg = args.split()
        if not arg:
            print("** class name missing **")
        elif arg[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in rep:
                if arg[1] == rep[obj_id].id:
                    print(rep[obj_id])
                    match = True
            if match is not True:
                print("** no instance found **")

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
