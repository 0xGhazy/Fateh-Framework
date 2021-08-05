

import sys
from os import system
from termcolor import colored
from cores.HTTPHandler import HTTPHandler
from cores.help_manager import help_man, banner
from cores.Functions import check_host, check_port, generate_shell



# Normal terminal
TOOL_TERMINAL = colored("F4T3H> ", "green")








def check_py_version():
    py_version = sys.version_info[0]
    if py_version != 3:
        print(colored("[-] Python 3.x is required.", "red"))
        print(colored("[-] Run it with python3", "red"))
        exit()
    else:
        system("clear")


def main():
    system("clear")
    check_py_version()
    banner()
    
    while True:
        try:
            command = input(TOOL_TERMINAL)
            if int(command) < 0 or int(command) > 4:
                print(colored("~_~", "red"))
        except ValueError:
            pass

        if command == "":
            print(colored("~_~", "red"))
            
                
        elif command == "new" or command == "1":
            generate_shell()

        elif command == "ls-conn" or command == "2":
            pass

        elif command == "listening" or command == "3":
            rhost = input(colored("RHOST> ", "blue"))
            rport = int(input(colored("RPORT> ", "blue")))
            HTTPHandler(check_host(rhost), check_port(rport))

        elif command == "help" or command == "4":
            help_man()

        elif command == "exit" or command == "0":
            exit(0)

        else:
            system(command)


if __name__ == '__main__':
    main()