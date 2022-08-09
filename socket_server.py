#!/usr/bin/env python3

# socket
# well-known ports 0-1023 are reserved for system use
# well-known ports 1024-49151 are reserved for private use
# well-known ports 49152-65535 are reserved for public use

import socket

# tcp socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 50000))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"data: {data}, addr: {addr}")
                conn.sendall(b"Received: " + data)

# udp socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("127.0.0.1", 50000))
    while True:
        data, addr = s.recvfrom(1024)
        print(f"data: {data}, addr: {addr}")
        s.sendto(b"Received: " + data, addr)