from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import mimetypes

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Serve HTML or JSON content based on the requested resource
        if '''Insert your code here'''== "text/html":
            try:
                '''
                Insert your code here.    


                '''                  
            except FileNotFoundError:
                '''Insert your code here'''
        elif '''Insert your code here''' == "application/json":
            try:
                '''
                Insert your code here.    


                ''' 
            except FileNotFoundError:
                '''Insert your code here'''
        else:
            # Handle unsupported content type
            '''
            Insert your code here.    


            ''' 
# Server setup
port = 8070
server_address = ('', port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving on port {port}")
httpd.serve_forever()