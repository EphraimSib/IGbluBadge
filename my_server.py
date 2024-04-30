#!/usr/bin/env python3

import http.server
import socketserver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import getpass

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Open Instagram login page
    driver.get('https://www.instagram.com/accounts/login/')

def get_credentials():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")  # Securely input the password
    return username, password
    
    # Log in
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    # Wait for the login to complete
    WebDriverWait(driver, 10).until(EC.url_to_be('https://www.instagram.com/'))

def main():
    # Get user credentials
    username, password = get_credentials()

    # You can save the credentials to a file or use them as needed
    # For security reasons, avoid storing passwords in plain text files

    print(f"Credentials saved for user: {username}")


    # Check if the user has a blue badge (verified account)
    blue_badge_element = driver.find_element(By.CSS_SELECTOR, 'svg[aria-label="Verified"]')
    blue_badge_status = blue_badge_element.is_displayed()

    if blue_badge_status:
        print("Congratulations! You have a blue badge (verified account) on Instagram.")
    else:
        print("You do not have a blue badge on Instagram.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()

# Set the desired port (e.g., 8080)
PORT = 8080

# Define a custom request handler
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response (optional)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello, this is your custom server!")

# Create the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Server is running on port {PORT}")
    httpd.serve_forever()





