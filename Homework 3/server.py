# Po-Shen Lee
# server.py

import socket


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break

        # Convert the byte data to an integer
        received_integer = int(data.decode())
        print(f"Received integer: {received_integer}")

        # Add 100 to the received integer
        result = received_integer + 100

        # Send the result back to the client as bytes
        conn.send(str(result).encode())
        print(f"Sent result: {result}")

        conn.close()


if __name__ == "__main__":
    start_server()
