#!/usr/bin/python

# UploadServer.py
#   in this file you will find all about abload server which make you able to
#   send files to the target machine. it's a simple http python server.

import os
from Configurations import UPLOADING_SERVER_ROOT_PATH
from Functions import attacker_address, checking_requirements
from termcolor import colored


local_host = attacker_address()[0]
public_host = attacker_address()[1]
port = 8080


def configUploadServer():
    PATH_CONTENT = os.listdir(UPLOADING_SERVER_ROOT_PATH)
    print(colored("[+] Starting UploadServer.py Script.", "green"))
    print("[ 1 ] For LAN Attacking\n[ 2 ] For WAN Attacking")
    try:
        attack_type = int(input(colored("Attack-Type>> ", "yellow")))
        while attack_type > 2 or attack_type < 1:
            print(colored("~_~", "red"))
            attack_type = int(input(colored("Attack-Type>> ", "yellow")))
        if attack_type == 1:
            print(colored("[+] LAN Attacking", "green"), colored(f"http://{local_host}:{port}","red"))
            for i in PATH_CONTENT:
                if os.path.isfile(i):
                    print(colored(f"- http://{local_host}:{port}/{i}", "green"))
                return local_host
        else:
            print(colored("[+] WAN Attacking", "green"), colored(f"http://{public_host}:{port}","red"))
            for i in PATH_CONTENT:
                print(colored(f"- http://{public_host}:{port}/{i}", "green"))
                return public_host
    except ValueError:
        print(colored("[-] Integer value only :(", "red"))
        exit()
    

def start_server(host, port):
    try:
        print(colored("\nCtrl+C to terminate the server\n", "yellow"))
        os.system(f"python3 -m http.server {str(port)}")
    except InterruptedError as error:
        print("[-] Server Terminated")


if __name__ == '__main__':
    checking_requirements()
    host = configUploadServer()
    start_server(host, port)


# TODO: make this file run from F4T3H.py file, without new terminal window.
# TODO: Update list dir to be walk method.
