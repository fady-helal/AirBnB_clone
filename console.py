#!/usr/bin/python3
"""Model for console."""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    valid_classes = ["BaseModel", "User", "Amenity",
                        "Place", "Review", "State", "City"]

    def quit(self, line):
        """exit the program"""
        return True

    def do_EOF(self, line):
        """exit the program , end of file."""
        return True

    def do_empty_line(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, args):
        """"""
        token = shlex.split(args)
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{token[0]}()")
            storage.save()
            print(new_instance.id)

    def show(self,args):
        """ Prints the string representation of an
            instance based on the class name and id
        """
        token = shlex.split(args)
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(token[0], token[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def destroy(self, args):
        """
        Deletes an instance based on the class name and id.
        """
        token = shlex.split(args)
        if len(token) == 0:
            print("** class name missing **")
        elif token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(token[0], token[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
    
    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        """
        objects = storage.all()
        token = shlex.split(arg)
        if len(token) == 0:
            for key, value in objects.items():
                print(str(value))
        elif token[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == token[0]:
                    print(str(value))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
