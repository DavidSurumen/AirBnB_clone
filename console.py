#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console module."""

    prompt = '(hbnb) '

    __classes = {
            "BaseModel"
            }

    def emptyline(self):
        """Do nothing if received an empty line."""
        pass

    def do_quit(self, line):
        """exit the interpreter."""
        return True

    def do_EOF(self, line):
        """exit by clicking Ctrl-D."""
        return True

    def postloop(self):
        """print a new line after interpreter is exited."""
        print()

    def help_quit(self):
        """doc for the quit command."""
        print("Quit command to exit the interpreter.\n")

    def help_EOF(self):
        """doc for EOF command."""
        print("Exits the interpreter when Crtl-D is pressed.\n")

    def do_create(self, args):
        """create command: create a new instance of BaseModel, save it, and
        print its id.\n
        Usage: create <class>
        """
        arg_list = args.split(' ')
        clas = arg_list[0]

        if clas:
            if clas not in HBNBCommand.__classes:
                print("** class doesn't exist **\n")
            else:
                obj = eval(clas)()
                obj.save()
                print(obj.id)
        else:
            print(" ** class name is missing **")

    def do_show(self, args):
        """show command: print the string representation of an instance
        based on class name and id.
        """
        obj_dict = storage.all()

        args_list = args.split(' ')
        clas = args_list[0]

        if not clas:
            print("** class name missing **")
        elif clas not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        else:
            id_ = args_list[1]
            key = '{}.{}'.format(clas, id_)

            if key not in obj_dict.keys():
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, args):
        """destroy command: deletes an instance based on class name and id,
        and save the changes into the JSON file."""

        obj_dict = storage.all()

        if len(args) == 0:
            print('** class name missing **')
        else:
            clas = args.split(' ')[0]
            if clas not in HBNBCommand.__classes:
                print('** class doesn\'t exist **')
            elif len(args.split(' ')) == 1:
                print('** instance id missing **')
            else:
                id_ = args.split(' ')[1]
                key = '{}.{}'.format(clas, id_)
                if key not in obj_dict.keys():
                    print('** no instance found **')
                else:
                    del obj_dict[key]
                    storage.save()

    def do_all(self, args):
        """all command: prints all string representation of all instances
        based or not on the class name."""

        clas = args.split(' ')[0]
        obj_dict = storage.all()

        if clas and clas not in HBNBCommand.__classes:
            print('** class doesn\'t exist')
        else:
            for key in obj_dict.keys():
                print(obj_dict[key])

    def do_update(self, args):
        """update command: updates an instance based on the class name
        and id by adding or updating an attribute, and save the chang
        into the JSON file.\n
        Usage <class name> <id> <attribute name> "<attribute value>"
        """
        obj_dict = storage.all()
        args_list = args.split(' ')

        clas = args_list[0]

        if not clas:
            print('** class name missing **')
        elif args_list[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist')
        elif len(args_list) == 1:
            print('** instance id missing **')
        else:
            key = '{}.{}'.format(args_list[0], args_list[1])
            if key not in obj_dict.keys():
                print('** instance not found **')

            elif len(args_list) == 2:
                print('** attribute name missing **')

            elif len(args_list) == 3:
                print('** value missing **')

            else:
                attrb = args_list[2]
                val = args_list[3]

                obj_dict[key].__dict__[attrb] = val
                obj_dict[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
