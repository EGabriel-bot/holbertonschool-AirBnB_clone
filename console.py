#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
import json


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

    def do_all(self, args):
        'Prints all string representation of all instances based or not on the class name'
        rep = storage.all()
        if args != BaseModel.__name__:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in rep:
                obj_list.append(rep[obj].__str__())
            print("{}".format(obj_list))

    def do_destroy(self, args):
        'Deletes an instance based on the class name and id\n'
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
                    try:
                        match = True
                        del rep[obj_id]
                        with open("file.json", 'w', encoding="utf-8") as json_file:
                            json_file.write(json.dumps(rep))
                        break
                    except KeyError:
                        pass

            if match is not True:
                print("** no instance found **")

    def do_update(self, args):
        'Updates an instance\n'
        arg_list = args.split()
        all_objs = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] != BaseModel.name:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            match = False
            for obj_id in all_objs.keys():
                if arg_list[1] == all_objs[obj_id].id:
                    match = all_objs[obj_id]
            if match is False:
                print("** no instance found **")
            else:
                if len(arg_list) == 2:
                    print("** attribute name is missing **")
                elif len(arg_list) == 3:
                    print("** value is missing **")
                else:
                    setattr(match, arg_list[2], arg_list[3])

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
