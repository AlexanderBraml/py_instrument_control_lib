import socket

server_ip = '132.231.14.104'  # Ändern Sie dies auf die IP-Adresse Ihres Servers
server_port = 5025  # Ändern Sie dies auf den Port Ihres Servers

cmd = '*IDN?\n'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

client_socket.sendall(cmd.encode())

response = client_socket.recv(1024)

response = response.decode()

print("Response:", response)

client_socket.close()
