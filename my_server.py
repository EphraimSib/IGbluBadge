#!/usr/bin/env python3

import http.server
import socketserver

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
