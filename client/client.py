    #!/usr/bin/env python3

import socket
import select
import errno

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 8080

my_username = input("Username >> ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode('utf-8')
username_header = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
client_socket.send(username_header + username)