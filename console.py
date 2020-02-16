#!/usr/bin/python3



import cmd
import models
from models.base_model import BaseModel
from models.user import User

all_class = {"BaseModel": BaseModel, "User": User}

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_create(self, inp):
        words = str.split(inp)
        kwargs = {}
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        if (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        else:
            instance = all_class[words[0]](**kwargs)
            instance.save()
            print(instance.id)

    def do_show(self, inp):
        words = str.split(inp)
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        if (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        if (len(words) < 2):
            print("** instance id missing **")
            return (False)
        if (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        key = words[0] + "." + words[1]
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, inp):
        words = str.split(inp)
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        if (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        if (len(words) < 2):
            print("** instance id missing **")
            return (False)
        key = words[0] + "." + words[1]
        if key in models.storage.all():
            models.storage.all()[key].delete()
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, inp):
        words = str.split(inp)
        new_list = []
        if (len(words) == 0):
            for value in models.storage.all().values():
                new_list.append(str(value))
        elif (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        else:
            for key in models.storage.all():
                if key.startswith(words[0]):
                        new_list.append(str(models.storage.all()[key]))
        print (new_list)

    def do_update(self, inp):
        words = str.split(inp)
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        elif (len(words) < 2):
            print("** instance id missing **")
            return (False)
        elif (len(words) < 3):
            print("** attribute name missing **")
            return (False)
        elif (len(words) < 4):
            print("** value missing **")
            return (False)
        else:
            if words[0] not in all_class:
                print("** class doesn't exists **")
            else:
                key = words[0] + "." + words[1]
                if key in models.storage.all():
                    setattr(models.storage.all()[key], words[2], words[3])
                    models.storage.all()[key].save()

    def do_quit(self, inp):
        """Quit command to exit the program\n"""
        return True
    def emptyline(self):
        pass

    do_EOF = do_quit

if __name__ == '__main__':
    p = HBNBCommand()
    p.cmdloop()
