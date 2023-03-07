from MyLib.files import conductor
import MyLib.errors as error
import constants


def main():
    cond = conductor.Conductor()
    er = error.Errors()
    s = " "

    while True:
        if constants.Const.textfile.is_open():
            print("\033[32m{}\033[0m".format(constants.Const.textfile.get_path()))
        elif constants.Const.csvfile.is_open():
            print("\033[32m{}\033[0m".format(constants.Const.csvfile.get_path()))
        else:
            print("\033[32m{}\033[0m".format(constants.Const.fold.get_path()))
            for i in constants.Const.fold.get_elements():
                print(f"{s:>5}{i}")

        command = input("введите команду: ").split()

        if len(command) == 0 or len(command) > 3:
            er.command_error()

        elif len(command) == 1:
            if command[0] == "exit":
                exit("программа заверена")
            else:
                er.command_error()

        elif len(command) == 2:
            match command[0], command[1]:
                case "print", "data":
                    cond.print_data()
                case "write", "data":
                    cond.write_data()
                case "delete", "data":
                    cond.delete_data()
                case "add", "data":
                    cond.add_data()
                case _, _: er.command_error()

        elif len(command) == 3:
            match command[0]:
                case "create":
                    cond.create_object(command[1], command[2])
                case "open":
                    cond.open_object(command[1], command[2])
                case "close":
                    cond.close_object(command[1], command[2])
                case "delete":
                    cond.delete_object(command[1], command[2])
                case _: er.command_error()


if __name__ == "__main__":
    main()
