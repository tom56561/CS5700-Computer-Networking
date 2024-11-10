# Po-Shen Lee
# server.py

from socket import *
import sys

if len(sys.argv) != 2:
    print("Usage: python server.py <port>")
    sys.exit(1)

serverPort = int(sys.argv[1])

# Retrieve server IP address dynamically
try:
    tempSocket = socket(AF_INET, SOCK_DGRAM)
    tempSocket.connect(('8.8.8.8', 80))
    serverIP = tempSocket.getsockname()[0]
    tempSocket.close()
except Exception:
    serverIP = '127.0.0.1'  # Fallback to localhost

print(f"server IP address: {serverIP}")
print(f"server port number: {serverPort}")
print("Ready to serve...")

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    connectionSocket, addr = serverSocket.accept()
    # Connection established
    while True:
        try:
            message = ''
            while True:
                data = connectionSocket.recv(1024).decode()
                if not data:
                    # Client closed connection
                    break
                message += data
                if '\r\n\r\n' in message:
                    # End of headers detected
                    break
            if not message:
                break  # No data received, exit inner loop
            # Process the HTTP request
            requestLines = message.splitlines()
            if len(requestLines) > 0:
                requestLine = requestLines[0]
                # Expected format: GET /filename HTTP/1.1
                parts = requestLine.split()
                if len(parts) >= 2 and parts[0] == 'GET':
                    filename = parts[1].lstrip('/')
                    # Now check if file exists
                    try:
                        with open(filename, 'r') as f:
                            outputdata = f.read()
                        # Send response
                        response = "HTTP/1.1 200 OK\n"
                        response += outputdata
                        connectionSocket.sendall(response.encode())
                    except IOError:
                        # File not found
                        response = "HTTP/1.1 404 Not Found\n"
                        connectionSocket.sendall(response.encode())
                else:
                    # Bad request
                    pass
            else:
                # Empty request
                pass
            # Continue to wait for next request from client
        except Exception as e:
            print(f"Exception: {e}")
            break
    connectionSocket.close()
