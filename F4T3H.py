
from os import system
from termcolor import colored
from cores.HTTPHandler import HTTPHandler
from cores.Data import banner
from cores.Functions import check_host, check_port
from cores.Functions import generate_shell
from cores.help_manager import help_man
from cores.Profile_Conf import TOOL_COMMAND_STATEMENT
from cores.Functions import check_py_version


def main():
    check_py_version()
    banner()
    
    while True:
        command = input(f"{TOOL_COMMAND_STATEMENT} ")
        if command == "":
            continue

        elif command == "gen-shell":
            generate_shell()


        elif command == "ls-conn":
            pass


        elif command == "listning":
            rhost = input("RHOST> ")
            rport = int(input("RPORT> "))
            HTTPHandler(check_host(rhost), check_port(rport))

        elif command == "help":
            help_man()


        elif command == "main":
            banner()


        elif command == "exit":
            quit()


        else:
            system(command)





if __name__ == '__main__':
    main()









# TODO:
# 1- Adding HTTPS (Encryption)
# 2- Fixing uploading/downloading problems.
# 3- Creating external modules
