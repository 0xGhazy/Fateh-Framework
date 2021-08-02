
import os
import sys
from cores.Profile_Conf import DESKTOP_PATH
def colored(text, col):
    return text


host = "YourIPAddressHere"
port = 8080

def uploadServerBanner():
    print("   __  __      __                __     _____                          ")
    print("  / / / /___  / /___  ____ _____/ /    / ___/___  ______   _____  _____")
    print(" / / / / __ \/ / __ \/ __ `/ __  /_____\__ \/ _ \/ ___/ | / / _ \/ ___/")
    print("/ /_/ / /_/ / / /_/ / /_/ / /_/ /_____/__/ /  __/ /   | |/ /  __/ /    ")
    print("\____/ .___/_/\____/\__,_/\__,_/     /____/\___/_/    |___/\___/_/     ")
    print("    /_/                                                                ")
    os.chdir(DESKTOP_PATH)
    print(f"[+] CWD: {DESKTOP_PATH}")
    print(f"[+] Now server is up @ http://{host}:{port}")
    print(f"[+] The link of files must be like: http://{host}:{port}/file_name\n")
    print('[+] All your Files in Desktop Dir:')
    files_inpath = os.listdir(DESKTOP_PATH)
    for i in files_inpath:
        print("\t", i)


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

if __name__ == '__main__':
    main()