import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '  # Set a custom prompt
    classes = ['BaseModel']

    def do_quit(self, line):
        """Exit the console."""
        return True

    def do_EOF(self, line):
        """
        End Of File -
            quit the program when user presses ctrl+D or ^Z and type exit
        """
        return True

    def emptyline(self):
        """
        Overwrite default behavior to repeat last cmd
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id. Ex: `$ create BaseModel`
        """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
            based on the class name and id
        """

        if len(line) == 0:
            print("** class name missing **")

        args = line.split()

        if args[0] not in self.classes:
            print("** class doesn't exist **")
        try:
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key not in storage.all().keys():
                print("** no instance found **")
            else:
                print(storage.all()[obj_key])

        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
            and id (save the change into the JSON file).
        """
        if len(line) == 0:
            print("** class name missing **")

        args = line.split()

        if args[0] not in self.classes:
            print("** class doesn't exist **")
        try:
            obj_key = f"{args[0]}.{args[1]}"
            if obj_key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[obj_key]
                storage.save()

        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
            based or not on the class name. Ex: `$ all BaseModel`
        """
        all_instances = []
        args = line.split()
        if len(line) == 0:
            for obj in storage.all().values():
                all_instances.append(obj.__str__())
            print(all_instances)
        elif args[0] in self.classes:
            for key, value in storage.all().items():
                if args[0] in key:
                    all_instances.append(value.__str__())
            print(all_instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
         Updates an instance based on the class name and id by adding or
            updating attribute (save the change into the JSON file).
            Ex: $ `update BaseModel 1234-1234-1234 email "aibnb@mail.com"`
        """
        args = line.split()
        if len(line) > 4:
            key = "{}.{}".format(args[0], args[1])
            cast = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip('"')
            arg3 = arg3.strip("'")
            setattr(storage.all()[key], args[2], cast(arg3))
            storage.all()[key].save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")


def parse(line):
    return tuple(line.split())


if __name__ == '__main__':
    HBNBCommand().cmdloop()
