#!/usr/bin/env python3

import os
import sys
import time
import re
import subprocess

def check_root():
    return os.geteuid() == 0

def main():
    print("\033[92mCHECKING IF YOU'RE ROOTED...")
    loading_symbols = ["/", "-", "\\", "|"]
    i = 0
    while True:
        print(f"\rLoading{loading_symbols[i % len(loading_symbols)]}", end="")
        i += 1
        time.sleep(10)
        if check_root():
            break

    if check_root():
        print("\033[92mYOU ARE ROOTED.")
    else:
        print("\033[92mYOU ARE NOT ROOTED.")

if __name__ == "__main__":
    main()

# Update packages and install dependencies
subprocess.run(["sudo", "apt-get", "update"])
subprocess.run(["sudo", "apt-get", "install", "-y", "php", "git", "curl", "python3", "ruby", "tor", "bash", "python3-pip", "xidel", "python3-selenium"])

# Install npm
subprocess.run(["sudo", "apt-get", "install", "-y", "npm"])

# Display info
print("\033[92m\n\n")
print("\033[92m ______                          _____        ______              _____        ______       _____                   ")
print("\033[92m |     |     |       |     |     |            |     |     /\     |      \     |            |                        ")
print("\033[92m |_____/     |       |     |     |____        |_____/    /  \    |       |    | ____       | ____                   ")
print("\033[92m |     \     |       |     |     |            |     \   /____\   |       |    |      \     |                        ")
print("\033[92m |_____|     |____   |_____|     |_____****** |_____|  /      \  |_____ /     |______|     |_____                   ")

print("\033[92m\n\n")
print("\033[92m         ***********************************************")
print("\033[92m         #                                             #")
print("\033[92m         #   tool For fishing IG credentials #")
print("\033[92m         #   Follow Me On Github: @ephraim sib#")
print("\033[92m         #   Contact Me In: ephraimsibale20@gmail.com#")
print("\033[92m         #   Changelog: 5-12-2023           #")
print("\033[92m         #                                             #")
print("\033[92m         ***********************************************")
print("\033[92m\n\n")


def run_server():
    while True:
        port = input("Please enter a port number (1024 to 65535): ")
        if validate_port(port):
            break
        else:
            print("Invalid port number. Please enter a valid port number.")

    # Generate the link
    link = f"http://localhost:{port}/"

    # Print the link
    print(f"Generated link: {link}")

    # Set the file to write log messages to
    logfile = "server.log"

    # Start the server (you need to define 'app' somewhere in your code)
    # app.run(port=port, logfile=logfile)

    # Save the user's credentials (you need to implement 'encrypt' function)
    username = input("Please enter your Instagram username: ")
    password = input("Please enter your Instagram password: ")
    with open("credentials.txt", "w") as f:
        f.write(f"{username}\n{password}")
    # Encrypt and save the credentials (you need to implement 'encrypt' function)
    # ...

    # Remove the plaintext credentials file
    os.remove("credentials.txt")
