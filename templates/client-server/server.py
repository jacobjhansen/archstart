import socket

IP = '127.0.0.1'
PORT = 4444

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Start the server on the defined IP and port
    server.bind((IP, PORT))

    # Start accepting connections to the server
    server.listen()
    connection, address = server.accept()

    # Wait for a client connection
    with connection:
        
        # Keep checking for data sent by the client
        while True:
            data = connection.recv(1024)
            if not data:
                break
            connection.send(data)
