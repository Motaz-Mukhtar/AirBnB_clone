#!/usr/bin/python3
"""This file contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb) "
    file = None

    __classes = [
            "BaseModel", "City", "State", "User", "Place", "Review", "Amenity"
        ]

    def do_EOF(self, arg):
        """Quit command to exit the program

        arg(list): list of all instances at __objects
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program

            arg(list): list of all instances at __objects
        """
        return True

    def emptyline(self):
        """ENTER will print emptyline.\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel

            arg(list): list of all instances at __objects
        """
        args = arg.split(' ')
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_model = eval(args[0] + "({})".format(", ".join(args[1: ])))
            print(new_model.id)
            new_model.save()

    def do_show(self, arg):
        """Prints the string representaton of
            an instance based on the class name and id

            arg(list): list of all instances at __objects
        """
        try:
            if not arg:
                raise SyntaxError
            arg_list = arg.split(" ")
            if arg_list[0] not in HBNBCommand.__classes:
                raise NameError
            if not arg_list[1]:
                raise IndexError

            instances = storage.all()
            key = arg_list[0] + "." + arg_list[1]

            print(storage._FileStorage__objects[key])

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes the instance that has
            the cmd arg (class name and id)

            arg(list): list of all instances at __objects
        """
        arg_list = arg.split(" ")
        if not arg:
            print("** class name missing **")
            return None
        elif (arg_list[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
            return None
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_count(self, arg):
        """ print the count of instances of a class

            arg(list): list of all instances at __objects
        """
        count = 0
        for key in storage.all().keys():
            if arg in key:
                count += 1
        print(count)

    def do_all(self, arg):
        """Prints all string repr. of
        all instances based or not on the class name

            arg(list): list of all instances at __objects
        """
        arg_list = arg.split(" ")
        obj_list = []

        if not arg:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)

        elif (arg_list[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                if value.__class__.__name__ == arg:
                    obj_list.append(value.__str__())
            print(obj_list)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id

            arg(list): list of all instances at __objects
        """
        arg_list = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif (arg_list[0] not in HBNBCommand.__classes):
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(arg_list[0], arg_list[1])
            if (key not in obj):
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                setattr(obj[key], arg_list[2], arg_list[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
