# Po-Shen Lee
# client.py

import socket
import sys


def send_integer_to_server(integer):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Send the integer to the server
    client_socket.send(str(integer).encode())

    # Receive the result from the server
    data = client_socket.recv(1024)
    print(f"Sent {integer} and received {data}")

    client_socket.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        # Get the integer from the command line
        integer = int(sys.argv[1])

        # Send the integer to the server and get the result
        send_integer_to_server(integer)

    except ValueError:
        sys.exit(1)
