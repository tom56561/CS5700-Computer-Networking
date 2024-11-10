# Po-Shen Lee
# client.py
 
from socket import *
import sys

# Check for correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python client.py <server IP> <port> <filename>")
    sys.exit(1)

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
filename = sys.argv[3]

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
try:
    clientSocket.connect((serverIP, serverPort))
except Exception:
    print("Error while connecting!")
    sys.exit(1)

# Send HTTP GET request
request = f"GET /{filename} HTTP/1.1\r\nHost: {serverIP}\r\n\r\n"
clientSocket.sendall(request.encode())

# Signal that we're done sending data
clientSocket.shutdown(SHUT_WR)

# Receive response from the server
response = ''
while True:
    try:
        data = clientSocket.recv(1024).decode()
        if not data:
            break
        response += data
    except Exception:
        break

clientSocket.close()

if response:
    print("Connection Successful!")
    print("---------------HTTP RESPONSE---------------")
    print(response.strip())
    print("---------------END OF HTTP RESPONSE---------------")
else:
    print("No response received.")
