# Po-Shen Lee

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        file_type, _ = mimetypes.guess_type(self.path)

        if file_type == "text/html":
            try:
                # Serve the HTML file if it exists
                with open(self.path[1:], 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                # Send 404 if the HTML file is not found
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><body><h1>404 Not Found</h1></body></html>")
        elif file_type == "application/json":
            try:
                # Serve the JSON file if it exists
                with open(self.path[1:], 'rb') as file:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(file.read())
            except FileNotFoundError:
                # Send 404 if the JSON file is not found
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(
                    b"<html><body><h1>404 Not Found</h1></body></html>")
        else:
            # Handle unsupported content type
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found - Unsupported Content Type")


# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()
