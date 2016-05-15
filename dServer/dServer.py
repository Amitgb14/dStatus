# -*- coding: utf-8 -*-

import socket
import sys

_msg = "ping"


def connect(HOST="localhost", PORT=9999):
    """
    This is Client application act as a Server
    """
    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server and send ping
    sock.connect((HOST, PORT))
    sock.sendall(_msg)

    # Receive data from the server and shut down
    received = sock.recv(2024)
    sock.close()
    return received
