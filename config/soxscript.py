#!/usr/bin/env python3

import socket

HOST = 'vacuum.lan'
PORT = 7777

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(5)
    sock.connect((HOST, PORT))
    sock.sendall(";1.0;".encode())
    output = sock.recv(256)

print(output)