
from termcolor import colored

def banner():
    print(colored(f"""\033[1m
     ___ _ _ _____ _____  _   __      ___      ___ ___ 
    | __| | |_   _|__ / || |__\ \    / (_)_ _ / __|_  )
    | _||_  _|| |  |_ \ __ |___\ \/\/ /| | ' \ (__ / / By:{colored("0xGhazy", "red")}\033[93m
    |_|   |_| |_| |___/_||_|    \_/\_/ |_|_||_\___/___|\n
    > Script Options:        > Description
    -----------------        -------------
    [1] new                  - Generating a new Shell.
    [2] ls-conn              - List all incoming connections/sessions.
    [3] listening            - Starting shell session.
    [4] help                 - Help man.
    [0] exit                 - Exit this awesome tool :(\n""", "yellow"))


