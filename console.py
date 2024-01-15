#!/usr/bin/python3
"""
Console module for the AirBnB project.
"""
import cmd
import shlex
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""
    prompt = "(hbnb) "

    class_dict = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
                  "Place": Place, "Review": Review, "State": State,
                  "User": User}

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_EOF(self, arg):
        """Exit the console."""
        return True

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_create(self, arg):
        """Create a new instance of a specified class."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.class_dict[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of all instances."""
        args = shlex.split(arg)
        objects = storage.all()
        obj_list = []
        if not args:
            for obj_id, obj in objects.items():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            for obj_id, obj in objects.items():
                if args[0] == obj.__class__.__name__:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            objects = storage.all()
            if key in objects:
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(objects[key], args[2], args[3])
                    storage.save()
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()