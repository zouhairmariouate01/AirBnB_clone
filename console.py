#!/usr/bin/env python3

import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models import storage

"""
    Module of console.

    console is an interpreter tool used to manage data of the project.

    USE:
    ----
        >>> ./console
        (hbnb)
"""


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
        Class of console.
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Review": Review,
        "Amenity": Amenity
    }

    def default(self, arg):
        """
            Method of default behavior for cmd module
            when input is invalid.
        """
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def emptyline(self):
        """
            emptyline - function that prints an empty line.
        """
        pass

    def do_quit(self, line):
        """
            Method that exits the program.
            Return:
                value (bool): True
        """
        return True

    def do_EOF(self, line):
        """
            Method that exits the program.
            Return:
                value (bool): True
        """
        print("")
        return True

    def do_create(self, line=None):
        """
            Method that create new instances from Classes.
            Usage: create <class>
        """
        if line is None or line == "":
            print("** class name missing **")
        else:
            if line not in self.classes:
                print("** class doesn't exist **")
            else:
                instance = self.classes[line]()
                instance.save()
                print(instance.id)

    def do_show(self, line=None):
        """
            Method shows the data of a specific object by
            The Class Name and Id.
            Usage:
                show <class>
                show <class> id
                <class>.show()
                <class>.show(id)
        """

        all = storage.all()

        if line is None:
            return
        words = line.split(" ")
        if len(words) == 0 or line == "":
            print("** class name missing **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif words[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if words[1][0] == "\"" and words[1][-1] == "\"":
                words[1] = words[1][1:-1]
            full_name = f"{words[0]}.{words[1]}"
            if full_name not in all:
                print("** no instance found **")
            else:
                print(all[full_name])

    def do_destroy(self, line):
        """
            Method that removes an object using its
            Class nams and id.
            Usage:
                destroy <class> id or <class>.destroy(id)
        """

        if line is None:
            return
        words = line.split(" ")
        if len(words) == 0 or line == "":
            print("** class name missing **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif words[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            full_name = f"{words[0]}.{words[1]}"
            if full_name not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[full_name]

    def do_all(self, line=None):
        """
            Method that prints all objects based on its class name
            or not, as a string list.
            Usage: all or <class>.all()
        """

        all = storage.all()

        if line is None:
            return
        if line == "":
            obj_list = [f"{k}" for k in all.values()]
            print(obj_list)
        else:
            if line.strip() not in self.classes:
                print("** class doesn't exist **")
            else:
                obj_list = []
                for o in all.values():
                    if line.strip() == o.__class__.__name__:
                        obj_list.append(o.__str__())
                print(obj_list)

    def do_count(self, arg):
        """
            Method that counts the number of instances saved.
            Usage: count <class> or <class>.count()
        """
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0].strip() == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line=None):
        """
            Method that updates object using the class name
            and object's id and attribute's name and the attribute value.
            Usage:
                update <class name> <id> <attribute name> "<attribute value>"
        """

        argl = parse(line)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in self.classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
