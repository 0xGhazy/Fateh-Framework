


def help_man():
    print("[+] F4T3H-C2 Help manager")
    while True:
        help_command = input(f"F4T3H(Help-Manager)> ").lower()

        if help_command == "ls networking":
            print("[+] All about networking module.")

        elif help_command == "exit":
            break

        else:
            print("[-] Sorry i can't understand you :(")