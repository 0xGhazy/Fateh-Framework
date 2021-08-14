

import os
import sys
import json
import folium
import socket
import geocoder
import requests
from datetime import datetime
from termcolor import colored
from socket import gethostbyname, inet_aton
from prettytable import PrettyTable
from Configurations import DEF_SHELL_PATH, CSS_CODE, HTML_TABLE_CODE, DESKTOP_PATH

def ip_lookup(ip_address):
  
    try:
        print(colored("[+] Getting geolocation for {}".format(colored(ip_address, "yellow")), "green"))
        ip_api = f"https://ipapi.co/{ip_address}/json/"
        api_response = requests.get(ip_api)
        ip_info = json.loads(api_response.content) # reading API response
        print(colored("[+] We have received the response from the API successfully", "green"))
        report_file_response = int(input("[?] Do you want to create HTML report (0/1)? "))
        while report_file_response > 1 or report_file_response < 0:
            report_file_response = int(input("[?] Do you want to create HTML report (0/1)? "))
        if report_file_response == 1:
            report_title = f"{ip_address}-report.html"
            os.chdir(DESKTOP_PATH)
            global HTML_TABLE_CODE
            HTML_TABLE_CODE = HTML_TABLE_CODE.format(ip_info['ip'], ip_info['country_name'],
                                                    ip_info['city'], ip_info['region'], ip_info['region_code'],
                                                    ip_info['country_capital'], 
                                                    ip_info['longitude'], ip_info['latitude'], ip_info['timezone'],
                                                    ip_info['country_calling_code'], ip_info['currency'],
                                                    ip_info['currency_name'], ip_info['languages'], ip_info['country_area'],
                                                    int(ip_info['country_population']), ip_info['asn'], ip_info['org'])
            geolocation = geocoder.ip(ip_address)
            ip_geolocation = geolocation.latlng
            my_map = folium.Map(location = ip_geolocation, zoom_start = 15)
            folium.CircleMarker(location = ip_geolocation, radius = 55).add_to(my_map)
            folium.Marker(ip_geolocation, popup = ip_info['city']).add_to(my_map)
            my_map.get_root().html.add_child(folium.Element(CSS_CODE))
            my_map.get_root().html.add_child(folium.Element(HTML_TABLE_CODE))
            my_map.save(report_title)
            os.system(f"firefox {report_title}")
        else:
            table = PrettyTable(["Attribute", "Value"])
            table.add_row(["IP Address", ip_info['ip']])
            table.add_row(["Country Name", ip_info['country_name']])
            table.add_row(["City", ip_info['city']])
            table.add_row(["Region", ip_info['region']])
            table.add_row(["Region Code", ip_info['region_code']])
            table.add_row(["Country Capital", ip_info['country_capital']])
            table.add_row(["Longitude", ip_info['longitude']])
            table.add_row(["Latitude", ip_info['latitude']])
            table.add_row(["Time Zone", ip_info['timezone']])
            table.add_row(["Country Calling Code", ip_info['country_calling_code']])
            table.add_row(["Currency", ip_info['currency']])
            table.add_row(["Currency Name", ip_info['currency_name']])
            table.add_row(["Country Language", ip_info['languages']])
            table.add_row(["Country Area (KM)", ip_info['country_area']])
            table.add_row(["Country Population (Person)", int(ip_info['country_population'])])
            table.add_row(["Asn", ip_info['asn']])
            table.add_row(["ISP-ORG", ip_info['org']])
            print(colored(table, "green"))
    except Exception as error_msg:
        print(colored(f"[-] Error MSG:\n{error_msg}\n", "red"))
        exit(0)


def port_scanner(ip_address, ports):
    socket_obj = socket.socket()
    print(f"[+] Starting port scanneing @ < {datetime.now()} >")
    print(f"[+] Target address: {ip_address} scanning for [{ports}] Ports")
    for port in ports.split(","):
        try:
            if socket_obj.connect_ex((str(ip_address), int(port))) == 0:
                print(colored(f"- Port {port} is open.", "green"))
            else:
                print(colored(f"- Port {port} is close.", "red"))
        except Exception as error:
            print(colored(f"Error MSG:\n{error}\n", "red"))


def attacker_address():
    EXTERNAL_IP_ADDRESS = requests.get('https://api.ipify.org').text
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    LOCAL_IP_ADDRESS = s.getsockname()[0]
    return (LOCAL_IP_ADDRESS, EXTERNAL_IP_ADDRESS)


def print_attacker_address():
    ips = attacker_address()
    print("[#] Your Local IP address:",colored(ips[0], "red"))
    print("[#] Your Public IP address:",colored(ips[1], "red"))


def checking_requirements():
    os.system("clear")
    # check python version
    pyVersion = sys.version_info[0]
    if pyVersion != 3:
        print(colored("[-] Python 3.x is required.", "red"))
        print(colored("[-] Run it with python3", "red"))
        exit()
    else:
        pass


def generate_shell():
    name = input("NAME>> ")
    if name == "end":
        return
    while name == "":
        name = input("NAME>> ")

    address = attacker_address()
    print("[-] For WAN Attacking use:", colored(address[0], "green"))
    print("[-] For LAN Attacking use:", colored(address[1], "green"))
    host = input("RHOST>> ")
    if host == "end":
        return
    while len(host) < 1:
        host = input("RHOST>> ")
    host = check_host(host)

    port = input("PORT>> ")
    if port == "end":
        return
    while len(port) <1:
        port = input("PORT>> ")
    port = check_port(int(port))

    with open(os.path.dirname(__file__) + "/shell.py", "r+") as source:
        content = source.read()
    content = content.replace("XHOST", host)
    content = content.replace("XPORT", str(port))

    path = DEF_SHELL_PATH + f"{name}.py"
    with open(path, "w+") as shell:
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
            return host
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


# TODO: adding vulnerability scanner.

