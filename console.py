#!/usr/bin/python3



import cmd
import models
from models.base_model import BaseModel

all_class = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "

    def do_create(self, inp):
        words = str.split(inp)
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        if (words[0] not in all_class):
            print("** class doesn't exist **")
            return (False)
        else:
            instance = BaseModel()
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
        else:
            print("** no instance found **")


    def do_quit(self, inp):
        """Quit command to exit the program\n"""
        return True
    def emptyline(self):
        pass

    do_EOF = do_quit

if __name__ == '__main__':
    p = HBNBCommand()
    p.cmdloop()
