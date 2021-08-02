
from os import system
from termcolor import colored

def banner():
    system("cls")
    print(f"""
     ___ _ _ _____ _____  _   __      ___      ___ ___ 
    | __| | |_   _|__ / || |__\ \    / (_)_ _ / __|_  )
    | _||_  _|| |  |_ \ __ |___\ \/\/ /| | ' \ (__ / / By:{colored("0xGhazy", "red")}
    |_|   |_| |_| |___/_||_|    \_/\_/ |_|_||_\___/___|

    > Script Options:        > Description
    -----------------        -------------
    new-shell                - Generating a new Shell with a spasific shell name, rhost, and rport.
    ls-conn                  - Display all incomming/saved connections from your clients.
    listning                 - Starting listining to incomming connections.
    help                     - Displaying help menue.
    main                     - Displaying this banner again.
    exit                     - Exit this awsome tool :(\n""")




def trans_module_help():
    return """
    [-] Trans-Module:
    -----------------
    send                                - Sending binary files from your 'SENDING_PATH' dir to target machine.\n
    get                                 - Downloading binary files from the target machine.\n
    exsent                              - Sending binary files from external resource to target machine.\n
    """

def networking_module_help():
    return """
    [-] Networking-Module:
    ----------------------
    port-scan                           - Scanning ip address for opened port numbers.
                                              F4T3H> scan <IP ADDRESS>:<PORT1,PORT2..>\n
    geoip                               - Getting information about ip address.\n
    list-connections                    - Display list of all connections.\n
    """

def system_module_help():
    return """
    [-] System-Management-Module:
    -----------------------------
    system-info                         - Display all system's information like 'systeminfo'\n
    whoami                              - Returning the Currant user and his statue if admin or not.\n
    add-user                            - Adding a new user to users list.\n
    del-user                            - Deleting user from users list.\n
    """

def file_module_help():
    return """
    [-] File-Mangaement:
    --------------------
    write                               - commsd65s4d6s4d5s4d645
                                        F4T3H> write <FILE NAME>\n
    delete                              - Deleting files from Directory.
                                        F4T3H delete <FILE Name>\n
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
    """

def cracking_module_help():
    return """
    [-] Cracking-Module:
    --------------------
    zip-crack
    """

def browser_module_help():
    return """
    [-] Browser-Module:
    -------------------
    read-cookies
    read-history
    """


