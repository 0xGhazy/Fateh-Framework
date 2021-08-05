from getpass import getuser
from termcolor import colored

# Default shell exporting path
DEF_SHELL_PATH = f"/home/{getuser()}/Desktop/"

# Server-Root path (for sending files)
SENDING_PATH = "/home/kali/Downloads/"

# Default Download Path
DESKTOP_PATH = DOWNLOADING_PATH = DEF_SHELL_PATH

# TODO:
# 1- updating shell statement to contain currant connected shell ip/cwd
# 2- updating uploadServer to accept the givin sending path.