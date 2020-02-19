#!/usr/bin/python3

""" Console """

import cmd
import models
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

all_class = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
             "Place": Place, "Review": Review, "State": State, "User": User}

integers = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]

floats = ["latitude", "longitude"]


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, inp):
        """ Creates a new instance of a given class """

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
        """ Prints the string representation of an instance
        based on the class name and id """

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
        """ Deletes an instance based on the class name and id """

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
        """ Prints all string representation of all
        instances based or not on the class name. """

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
        print(new_list)

    def do_update(self, inp):
        """  Updates an instance based on the class
        name and id by adding or updating attribute """

        words = str.split(inp)
        if (len(words) == 0):
            print("** class name missing **")
            return (False)
        elif (len(words) < 2):
            if words[0] not in all_class:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return (False)
        elif (len(words) < 3):
            key = words[0] + "." + words[1]
            if words[0] not in all_class:
                print("** class doesn't exist **")
            elif key not in models.storage.all():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
            return (False)
        elif (len(words) < 4):
            print("** value missing **")
            return (False)
        else:
            key = words[0] + "." + words[1]
            if words[0] not in all_class:
                print("** class doesn't exist **")
                return (False)
            if key not in models.storage.all():
                print("** no instance found **")
                return (False)
            else:
                if words[0] == "Place":
                    if words[2] in integers:
                        words[3] = int(words[3])
                    if words[2] in floats:
                        words[3] = float(words[3])
                key = words[0] + "." + words[1]
                if key in models.storage.all():
                    word_ok = words[3].replace('"', '')
                    setattr(models.storage.all()[key], words[2], str(word_ok))
                    models.storage.all()[key].save()

    def do_quit(self, inp):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ empty line """
        pass

    def do_EOF(sel, arg):
        """ exit console """
        return True

    def default(self, inp):
        words = inp.split(".")
        newlist = []
        count = 0
        if words[0] in all_class and words[1] == "all()":
            self.do_all(words[0])
        elif words[0] in all_class and words[1] == "count()":
            if (words[0] not in all_class):
                print("** class doesn't exist **")
                return (False)
            else:
                for key in models.storage.all():
                    if key.startswith(words[0]):
                        count += 1
                print(count)
        cp = words[1].split('"')
        cp2 = cp[0].strip('(')
        cp3 = words[1].split('{')
        if words[0] in all_class and cp2 == "show":
            self.do_show(words[0] + " " + cp[1])
        elif words[0] in all_class and cp2 == "destroy":
            self.do_destroy(words[0] + " " + cp[1])
        elif words[0] in all_class and cp2 == "update":
            if "{" not in words[1]:
                self.do_update(words[0]+" "+cp[1]+" "+cp[3]+" "
                               + cp[5])
            else:
                cp3[1] = cp3[1].strip(')')
                cp3[1] = "{" + cp3[1]
                cp3[1] = cp3[1].replace("'", '"')
                dicci = json.loads(cp3[1])
                for key, value in dicci.items():
                    a = words[0]+" "+cp[1] + " " + key + " " + str(value)
                    self.do_update(a)


if __name__ == '__main__':
    p = HBNBCommand()
    p.cmdloop()
