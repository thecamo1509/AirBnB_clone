#!/usr/bin/python3



import cmd


class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb) "
    def do_quit(self, inp):
        """Quit command to exit the program\n"""
        return True
    def emptyline(self):
        pass

    do_EOF = do_quit

if __name__ == '__main__':
    p = HBNBCommand()
    p.cmdloop()
