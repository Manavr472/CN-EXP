import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server's IP address and port to connect to
server_host = '127.0.0.1'  # Server's IP address (localhost in this case)
server_port = 12345      # Port the server is listening on

# Connect to the server
client_socket.connect((server_host, server_port))

# Receive data from the server
server_data = client_socket.recv(1024).decode()
print(f"Server says: {server_data}")

# Send data to the server
message = "Hello, server!"
client_socket.send(message.encode())

# Close the client socket
client_socket.close()
