import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_host = '127.0.0.1'  # Server's IP address (localhost in this case)
server_port = 12345      # Port to listen on
server_socket.bind((server_host, server_port))

# Listen for incoming connections (maximum 5 clients in the queue)
server_socket.listen(5)
print(f"Server is listening on {server_host}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send data to the connected client
    message = "Hello, client!"
    client_socket.send(message.encode())

    # Receive data from the connected client
    client_data = client_socket.recv(1024).decode()
    print(f"Client says: {client_data}")

    # Close the client socket
    client_socket.close()
