import socket

HOST = '127.0.0.1'  # The server's IP address
PORT = 4444         # The server's port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Connect to the server at the specified IP and port
    server.connect((HOST, PORT))

    # Send data to the server
    server.send(b'example data')
    print('The client sent: example data')

    # Receive data from the server
    data = server.recv(1024)
    print('The server replied with:', str(data, 'utf-8'))
