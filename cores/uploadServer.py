
import os
import sys
from Configurations import SENDING_PATH
from termcolor import colored
import requests
import socket

def local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


host = local_ip()
port = 8080
EXTERNAL_IP_ADDRESS = requests.get('https://api.ipify.org').text


def uploadServerBanner():
    print("   __  __      __                __     _____                          ")
    print("  / / / /___  / /___  ____ _____/ /    / ___/___  ______   _____  _____")
    print(" / / / / __ \/ / __ \/ __ `/ __  /_____\__ \/ _ \/ ___/ | / / _ \/ ___/")
    print("/ /_/ / /_/ / / /_/ / /_/ / /_/ /_____/__/ /  __/ /   | |/ /  __/ /    ")
    print("\____/ .___/_/\____/\__,_/\__,_/     /____/\___/_/    |___/\___/_/     ")
    print("    /_/                                                                ")
    print("[+] For WAN Attacking use:",colored(f"http://{EXTERNAL_IP_ADDRESS}:{port}","red"))
    print("[+] For WAN Attacking use:",colored(f"http://{host}:{port}","red"))
    print(f"[+] All your Files in Sending Dir", colored(SENDING_PATH, "yellow"))
    print(colored(f"[+] The link of files must be like: http://{host}:{port}/file_name\n", "green"))
    files_inpath = os.listdir(SENDING_PATH)
    for i in files_inpath:
        print(colored(f"\thttp://{host}:{port}/{i}", "green"))


def check_py_version():
    print("[+] Checking your python version. . .")
    if int(sys.version_info[0]) != 3:
        print("[-] Python 3.x is required.")
        print("[-] Run it with python3")
        exit()
    else:
        os.system("clear")


def start_server(host, port):
    try:
        uploadServerBanner()
        os.system(f"python3 -m http.server {str(port)}")
    except Exception as error:
        print(colored(f"[-] Error Message: \n{str(error)}", "red"))


def main():
    check_py_version()
    start_server(host, port)

main()