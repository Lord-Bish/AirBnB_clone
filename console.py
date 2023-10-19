#!/usr/bin/python3
"""entry point to command interpreter"""

import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """command interpreter"""

    prompt = "(hbnb) "
    kls = ["BaseModel", "User", "Place", "State", "Amenity", "Review", "City"]

    def help_quit(self):
        """help quit"""
        print("quit command to exit the program\n")

    def do_quit(self, line):
        """exits the interpreter"""
        return True

    def help_EOF(self):
        """Shows docummented commands and their usage"""
        print("EOF command to quit the program\n")

    def do_EOF(self, line):
        """exits the enterpreter when hits cntr D"""
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, classname):
        """creates new instance of BaseModel"""
        if len(classname) == 0:
            print("** class name missing **")
        elif classname not in self.kls:
            print("** class doesn\'t exist **")
            return False

        else:
            new = eval("{}()".format(classname))
            new.save()
            print(new.id)

    def do_show(self, line):
        """Prints the string representation of instance"""
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return False

        elif args[0] not in self.kls:
            print("** class doesn\'t exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        all_objs = storage.all()
        for i in all_objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(all_objs[i])
                return False
        print("** no instance found **")

    def help_show(self):
        """help show"""
        print("show command shows instances\nbased on classname and id\n")

    def help_create(self):
        """help create"""
        print("create command creates new class\n")

    def help_destroy(self):
        """help destroy"""
        print("destroy command destroys class instances\n based on class name and id\n")

    def do_destroy(self, line):
        """
        Destroys instances based on class name and id
        """
        args = line.split()

        if len(args) == 0:
            print("** class name missing **")
            return False

        elif args[0] not in self.kls:
            print("** class doesn\'t exist **")
            return False

        elif len(args) < 2:
            print("** instance id missing **")
            return False

        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if i == "{}.{}".format(args[0], args[1]):
                    all_objs.pop(i)
                    storage.save()
                    return False
            print("** no instance found **")

    def help_all(self):
        """help all"""
        print("all command prints all string representation of all instances\n wether based on class name or not\n")

    def do_all(self, line):
        """
        print all string representation of all instances
        """
        args = line.split()
        all_objs = storage.all()

        if len(args) == 0:
            for i in all_objs:
                str_arg = str(all_objs[i])
                print(str_arg)

        elif line not in self.kls:
            print("** class doesn\'t exist **")
            return False

        else:
            for i in all_objs:
                if i.startswith(args[0]):
                    str_arg = str(all_objs[i])
                    print(str_arg)
        return False

    def help_update(self):
        """help update"""
        print("update command updates instance attributes\n")

    def do_update(self, line):
        """updates instance attributes"""
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            clsname = line.split()[0]
            eval("{}()".format(clsname))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            instanceid = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        all_objs = storage.all()
        try:
            clschange = all_objs["{}.{}".format(clsname, instanceid)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attributename = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            updatevalue = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if updatevalue.isdecimal() is True:
            setattr(clschange, attributename, int(updatevalue))
            storage.save()
        else:
            try:
                setattr(clschange, attributename, float(updatevalue))
                storage.save()
            except TypeError:
                setattr(clschange, attributename, str(updatevalue))
                storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
